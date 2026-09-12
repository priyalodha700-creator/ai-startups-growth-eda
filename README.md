# AI Startups — Growth Potential EDA & Prediction

Exploratory data analysis and a growth-potential prediction model built on a curated
list of 60 growing AI companies and startups (source: Exploding Topics, September 2024).

## 📌 Project Overview

The original data was published as a narrative PDF report, not a structured dataset.
This project:

1. Extracts and cleans the report into a structured CSV
2. Performs exploratory data analysis (EDA) on funding, founding year, location, and category
3. Builds an interpretable **Growth Potential Score (0–100)** using a weighted formula
4. Validates that score with a Logistic Regression classifier (5-fold cross-validation)

## 📂 Repository Structure

```
├── data/
│   ├── ai_startups_2024.csv        # Cleaned raw dataset (60 startups)
│   └── ai_startups_scored.csv      # Dataset with Growth Potential Score added
├── charts/
│   ├── 01_funding_vs_growth.png
│   ├── 02_founded_by_year.png
│   ├── 03_category_avg_growth.png
│   ├── 04_growth_status_pie.png
│   ├── 05_top_locations.png
│   ├── 06_top_bottom_growth_score.png
│   └── 07_feature_importance.png
├── code/
│   ├── build_csv.py                # PDF data → cleaned CSV
│   ├── eda.py                      # Exploratory data analysis + charts
│   └── growth_score_and_model.py   # Scoring formula + ML validation
└── README.md
```

## 🔍 Key Findings

- **Funding and search-growth are almost uncorrelated** (r ≈ -0.10) — raising more
  money does not reliably predict rising search interest.
- Most startups in the list were **founded between 2013 and 2019**, predating the
  2022 generative-AI boom.
- **San Francisco, California** is the dominant hub among these startups.
- A simple **Logistic Regression** trained only on raw features (search growth,
  company age, funding) reaches ~77% cross-validation accuracy at separating
  "high growth" vs "low growth" startups — a useful sanity check on the manual
  scoring formula, though not a production-grade model given the small (n=60) sample.

## 🧮 Growth Potential Score — Methodology

| Component | Weight | Reasoning |
|---|---|---|
| Search growth trend (log-scaled) | 40% | Leading indicator of rising interest |
| Company age (inverted) | 25% | Younger companies have more room to run |
| Funding raised (log-scaled) | 20% | Capital enables execution, diminishing returns |
| Growth status bonus | 15% | "Exploding" > "Regular" > "Peaked" |

## ⚠️ Limitations

- Small sample (60 startups), all pre-selected as already "growing" — no failure
  cases for comparison.
- Search growth is a proxy for interest, not a direct measure of revenue or users.
- Survivorship bias: large, already-successful companies (OpenAI, Anthropic) are
  included precisely because they succeeded.

## 🛠️ Tech Stack

Python · pandas · matplotlib · scikit-learn

## 📖 Source

Howarth, J. (2024, September 8). *60 Growing AI Companies & Startups (September 2024)*.
Exploding Topics.

---
Made by Priya, B.E. Data Science (3rd Semester), RNTU Bhopal.
