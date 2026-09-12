import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 120
df = pd.read_csv("/mnt/user-data/outputs/ai_startups_2024.csv")

# ---------- 1. Funding vs Search Growth scatter ----------
fig, ax = plt.subplots(figsize=(8, 6))
funded = df[df["funding_musd"] > 0]  # exclude bootstrapped for the log scale
ax.scatter(funded["funding_musd"], funded["search_growth_5yr_pct_numeric"], alpha=0.7, color="#2563eb")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Funding raised (US$ million, log scale)")
ax.set_ylabel("5-year search growth % (log scale)")
ax.set_title("Funding vs Search Growth (each dot = one startup)")
for _, row in funded.nlargest(5, "search_growth_5yr_pct_numeric").iterrows():
    ax.annotate(row["name"], (row["funding_musd"], row["search_growth_5yr_pct_numeric"]), fontsize=8)
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/01_funding_vs_growth.png")
plt.close()

# ---------- 2. Startups founded per year ----------
fig, ax = plt.subplots(figsize=(8, 5))
df["year_founded"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#16a34a")
ax.set_xlabel("Year founded")
ax.set_ylabel("Number of startups in list")
ax.set_title("When were these AI startups founded?")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/02_founded_by_year.png")
plt.close()

# ---------- 3. Category-wise average search growth ----------
fig, ax = plt.subplots(figsize=(9, 6))
cat_growth = df.groupby("category_group")["search_growth_5yr_pct_numeric"].mean().sort_values()
cat_growth.plot(kind="barh", ax=ax, color="#f59e0b")
ax.set_xlabel("Average 5-year search growth %")
ax.set_title("Which AI category is growing fastest (by search interest)?")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/03_category_avg_growth.png")
plt.close()

# ---------- 4. Growth status distribution ----------
fig, ax = plt.subplots(figsize=(6, 6))
df["growth_status"].value_counts().plot(kind="pie", autopct="%1.0f%%", ax=ax,
                                          colors=["#2563eb", "#f59e0b", "#94a3b8"])
ax.set_ylabel("")
ax.set_title("Search-growth status across the 60 startups")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/04_growth_status_pie.png")
plt.close()

# ---------- 5. Top locations ----------
fig, ax = plt.subplots(figsize=(8, 6))
df["location"].value_counts().head(10).sort_values().plot(kind="barh", ax=ax, color="#dc2626")
ax.set_xlabel("Number of startups")
ax.set_title("Top 10 startup hubs in this list")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/05_top_locations.png")
plt.close()

print("Correlation (funding vs growth %, funded-only, log-log):",
      funded[["funding_musd", "search_growth_5yr_pct_numeric"]].apply(lambda x: x if True else x)
      .corr().iloc[0, 1])
print("Median funding (all):", df["funding_musd"].median())
print("Median search growth %:", df["search_growth_5yr_pct_numeric"].median())
print("Charts saved.")
