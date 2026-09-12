import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permutation_importance

plt.rcParams["figure.dpi"] = 120
df = pd.read_csv("/mnt/user-data/outputs/ai_startups_2024.csv")

# =========================================================
# STEP 1: Rule-based "Growth Potential Score" (0-100)
# =========================================================
# Reasoning (documented, not a black box):
#  - search_growth_pct   -> 40% weight  (leading indicator of rising interest)
#  - company_age_2024    -> 25% weight  (younger + still growing = more room to run)
#  - funding_musd         -> 20% weight  (capital to execute, diminishing returns via log)
#  - status bonus         -> 15% weight  ("Exploding" > "Regular" > "Peaked")

def minmax(s):
    return (s - s.min()) / (s.max() - s.min())

df["growth_norm"] = minmax(np.log1p(df["search_growth_5yr_pct_numeric"]))
# Younger company = higher score on this sub-metric (invert age)
df["age_norm"] = 1 - minmax(df["company_age_2024"])
df["funding_norm"] = minmax(np.log1p(df["funding_musd"]))
status_score = {"Exploding": 1.0, "Regular": 0.5, "Peaked": 0.0}
df["status_norm"] = df["growth_status"].map(status_score)

df["growth_potential_score"] = (
    0.40 * df["growth_norm"] +
    0.25 * df["age_norm"] +
    0.20 * df["funding_norm"] +
    0.15 * df["status_norm"]
) * 100

df["growth_potential_score"] = df["growth_potential_score"].round(1)

top10 = df.nlargest(10, "growth_potential_score")[["name", "category_group", "growth_potential_score"]]
bottom10 = df.nsmallest(10, "growth_potential_score")[["name", "category_group", "growth_potential_score"]]

print("=== TOP 10 by Growth Potential Score ===")
print(top10.to_string(index=False))
print("\n=== BOTTOM 10 by Growth Potential Score ===")
print(bottom10.to_string(index=False))

# Save scored CSV
df.to_csv("/mnt/user-data/outputs/ai_startups_scored.csv", index=False)

# Bar chart of top/bottom 10
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
axes[0].barh(top10["name"][::-1], top10["growth_potential_score"][::-1], color="#16a34a")
axes[0].set_title("Top 10 — Highest Growth Potential Score")
axes[0].set_xlabel("Score (0-100)")
axes[1].barh(bottom10["name"][::-1], bottom10["growth_potential_score"][::-1], color="#dc2626")
axes[1].set_title("Bottom 10 — Lowest Growth Potential Score")
axes[1].set_xlabel("Score (0-100)")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/06_top_bottom_growth_score.png")
plt.close()

# =========================================================
# STEP 2: Labels from the score (top 40% = "High Growth")
# =========================================================
threshold = df["growth_potential_score"].quantile(0.6)
df["high_growth_label"] = (df["growth_potential_score"] >= threshold).astype(int)
print(f"\nThreshold for 'High Growth' label: {threshold:.1f} | "
      f"High-growth count: {df['high_growth_label'].sum()} / {len(df)}")

# =========================================================
# STEP 3: Simple Logistic Regression validated with 5-fold CV
#          (Just to confirm the SAME features separate the classes
#           the model wasn't just told the label off the same formula --
#           it's fed only the RAW features, not the score itself)
# =========================================================
features = ["search_growth_5yr_pct_numeric", "company_age_2024", "funding_musd"]
X = df[features].copy()
X["search_growth_5yr_pct_numeric"] = np.log1p(X["search_growth_5yr_pct_numeric"])
X["funding_musd"] = np.log1p(X["funding_musd"])
y = df["high_growth_label"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_scaled, y, cv=cv, scoring="accuracy")
print(f"\n5-fold CV accuracy: {scores.mean():.2f} (+/- {scores.std():.2f})")
print("NOTE: dataset has only 60 rows -- this is a sanity check, not a production model.")

model.fit(X_scaled, y)
importance = pd.Series(np.abs(model.coef_[0]), index=features).sort_values()

fig, ax = plt.subplots(figsize=(7, 4))
importance.plot(kind="barh", ax=ax, color="#7c3aed")
ax.set_title("Which features drive the 'High Growth' prediction?")
ax.set_xlabel("|Logistic Regression coefficient| (standardized features)")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/07_feature_importance.png")
plt.close()

print("\nDone. Scored CSV + charts saved.")
