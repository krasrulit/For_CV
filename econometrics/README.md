# Applied Econometrics — Causal Inference

Course projects from Applied Econometrics (Faculty of Economics, MSU, 2025/26). Each project estimates a causal effect from observational data and stress-tests the result. Code in Python; written reports and the original task statements are included.

---

## 1. Urban Wage Premium — does moving to a big city raise wages?

Path: `urban_wage_premium/`

Estimates the causal effect of relocating to a central city on monthly wages, using NLSY panel data (US, 1979–1994). Treatment = individuals who moved from a small town to a central city; control = those who never moved. The core challenge is selection: people who move differ systematically from those who stay.

**Methods**
- Covariate-balance checks with multiple-testing correction (Holm)
- Pair-regression baseline, with a discussion of why it is biased
- Mahalanobis-distance matching (1:1, no replacement) and post-matching balance
- Inverse probability weighting (IPW) on a propensity score, with stabilization, trimming, and weight capping
- Double-robust LASSO (double selection) for data-driven control selection
- Heterogeneous treatment effects via causal forest (T-learner), with bootstrap confidence intervals and a driver analysis

**Result.** The effect is positive across specifications (~125–290 wage units depending on imputation and method); statistical significance is sensitive to the small treatment group (72 treated vs. ~1,200 control). Heterogeneity analysis points to education and AFQT (an ability proxy) as the main drivers of effect size.

**Files:** `analysis.ipynb` · `report.pdf` · `task.pdf` · `wage_gap.xlsx` (data) · `NLS_Investigator_Search.pdf` (variable documentation)

---

## 2. Platform Price Parity — the Booking.com / Macron Law case

Path: `platform_price_parity/`

Estimates how France's ban on price-parity clauses affected hotel prices on Booking.com, loosely following Mantovani, Piga & Reggiani (*European Economic Review*, 2021). Treatment region = Corsica; control = Sardinia.

**Methods**
- Difference-in-differences with controls and triple interactions (chain vs. independent, star rating, hotel size) to test heterogeneity
- Synthetic control: a "synthetic Corsica" built from a weighted donor pool, with predictor-balance diagnostics
- Placebo tests in time and in space
- Robustness: leave-one-out on donors and an RMSPE pre/post fit-ratio criterion

**Result.** After the law, prices on Corsica fell ~2.5–3.3% relative to Sardinia (DiD), with larger drops for chain hotels and mid-tier (3–4 star) properties. Synthetic control confirms a widening gap after the cutoff (reaching ~14% by the final week); placebo and leave-one-out checks support the effect's robustness.

**Files:** `analysis.ipynb` · `report.pdf` · `task.pdf` · `data_mac_sr.dta` · `data_mac_synth.dta` · `data_mr_placebo.dta`

---

## Skills demonstrated

Causal inference on observational data · matching · propensity scores / IPW · double-robust LASSO · causal forests · difference-in-differences · synthetic control · placebo and robustness testing · bootstrap inference · Python (pandas, scikit-learn, statsmodels)
