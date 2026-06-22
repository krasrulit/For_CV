# Portfolio: algorithms, SQL, Python libraries, ML, econometrics & a finance project

This repository is a concise, hands-on overview of my practical skills. It collects solved algorithmic problems, SQL notes, walkthroughs of core Python libraries, applied econometrics projects, and a university investment-portfolio project.

## Quick navigation
- **[algorithms/](./algorithms)** — solved problems on algorithms and data structures
- **[python_libraries/](./python_libraries)** — my notes and walkthroughs of popular Python libraries
- **[ML/](./ML)** — machine-learning theory, practical cheat sheets, and a notebook
- **[econometrics/](./econometrics)** — applied causal-inference projects
- **[SQL/](./SQL)** — SQL function reference + practice problems
- **[finance_project/](./finance_project)** — university finance project (investment portfolio)

---

## Contents

### 1. [algorithms/](algorithms) — Algorithms
- Subfolder **Yandex_algorithms** — solutions to problems from Yandex's first algorithms training (homework 1).
- Subfolder **sum_algorithms** — LeetCode "sum" problems (`Two Sum`, `3Sum`, `4Sum`, `K-Sum`, etc.).

Skills: arrays and strings, hash maps, two pointers, sorting, basic data structures.

Full description: see [the folder's README](algorithms/README.md)

---

### 2. [python_libraries/](python_libraries) — Python libraries

My notes and practice problems for the core data-analysis and visualization libraries:

- **numpy/** — [Функции Numpy.ipynb](python_libraries/numpy/Функции%20Numpy.ipynb)
  Core `NumPy` functions: array creation, operations, statistics, transformations.

- **matplotlib/**
  - [Функции_matplotlib.ipynb](python_libraries/matplotlib/Функции_matplotlib.ipynb) — overview of the library's functions
  - [Функции_matplotlib2.ipynb](python_libraries/matplotlib/Функции_matplotlib2.ipynb) — continuation, example charts
  - [Задачи_matplotlib.ipynb](python_libraries/matplotlib/Задачи_matplotlib.ipynb) — practice problems
  - [Работа_с_картой.ipynb](python_libraries/matplotlib/Работа_с_картой.ipynb) — example of working with map data

- **seaborn/**
  - [Seaborn.ipynb](python_libraries/seaborn/Seaborn.ipynb) — functions and styling options
  - [Задачи_seaborn_1.ipynb](python_libraries/seaborn/Задачи_seaborn_1.ipynb), [Задачи_seaborn_2.ipynb](python_libraries/seaborn/Задачи_seaborn_2.ipynb) — practice problems
  - [Big_one_seaborn.ipynb](python_libraries/seaborn/Big_one_seaborn.ipynb) — a case study on a real dataset (fields: ProjectID, UserID, CompanyID, FileSize, TypeDocs, etc.), with visualization of distributions, activity, and relationships between users, projects, and companies.

- **pandas/**
  - [Pandas.pdf](python_libraries/pandas/Pandas.pdf) and [README.md](python_libraries/pandas/README.md) — a walkthrough of the library: `Series/DataFrame`, indexing, missing values (`isna/fillna/interpolate`), joins (`concat/merge/join`), `groupby/agg/transform`, window methods (`rolling/expanding/ewm`), CSV/Excel (including chunks), quick plots, and table formatting with `Styler`.

---

### 3. [econometrics/](econometrics) — Applied econometrics

Causal-inference projects from Applied Econometrics (MSU): estimating causal effects from observational data and stress-testing them.

- **Urban Wage Premium** — does moving to a big city raise wages? (NLSY panel). Matching, IPW on a propensity score, double-robust LASSO, heterogeneous effects via causal forest.
- **Platform Price Parity** — the effect of France's price-parity ban on Booking.com hotel prices. Difference-in-differences with triple interactions and synthetic control, with placebo and leave-one-out checks.

Full description: see [the folder's README](econometrics/README.md)

---

### 4. [finance_project/](finance_project) — Finance project

A coursework case: building an investment plan and portfolio for a fictional person (a 20-year-old student, FIRE adherent).

Project materials:
- [Проект_по_портфельному_менеджменту.xlsx](finance_project/Проект_по_портфельному_менеджменту.xlsx) — Excel calculations
- [Проект_по_портфельному_менеджменту.pdf](finance_project/Проект_по_портфельному_менеджменту.pdf) — presentation
- [final_code.ipynb](finance_project/final_code.ipynb) — calculations and modeling in a Jupyter notebook

The folder's `README.md` describes the case goals and starting conditions, the asset structure and currency diversification, the savings and rebalancing plan, and the risk profile / FIRE philosophy.

---

### 5. [SQL/](SQL) — SQL

Two compiled PDFs on SQL (MySQL 8+):

- [Функции_SQL.pdf](SQL/Функции_SQL.pdf) — my own SQL reference with examples (filtering, aggregation, JOINs, subqueries, dates/strings/regex, `@` variables, CTEs, and window functions).
- [Примеры_запросов.pdf](SQL/Примеры_запросов.pdf) — a set of problems with solutions (each laid out as "Database → Task → Solution → Explanation").

The folder also includes a task map by topic (`JOIN`, `GROUP BY`, window functions, CTEs, etc.) for easy navigation.

---

### 6. [ML/](ML) — Machine Learning

ML materials: a theory summary, two practical cheat sheets, and a starter notebook.

- [ML_Практическая_справка.pdf](ML/ML_Практическая_справка.pdf) — core techniques and code templates: an ML-project checklist, data prep (`pandas/NumPy`, `SimpleImputer`, `StandardScaler/MinMaxScaler`, `OneHotEncoder`), splitting and validation (`train_test_split`, `KFold/StratifiedKFold`, `cross_val_score`), `Pipeline/ColumnTransformer` without data leakage, metrics and baselines (`Dummy*`, `accuracy/precision/recall/F1`, `ROC-AUC`, `MSE/MAE/R²`), hyperparameter tuning (`GridSearchCV/RandomizedSearchCV`), saving artifacts (`joblib`), and handling imbalance (`class_weight`, stratification).
- [ML_Практическая_справка_2.pdf](ML/ML_Практическая_справка_2.pdf) — recipes: `DBSCAN` (k-distance plot, `cosine`/`haversine`), clustering evaluation (silhouette, Dunn index), `OLS/Ridge/Lasso/Logistic` regressions, `PCA`, ensembles (`RandomForest`, `CatBoost/XGBoost/LightGBM`), blending/stacking.
- [ML_Теория.pdf](ML/ML_Теория.pdf) — theoretical foundations: overfitting and cross-validation, `GD/SGD`, `kNN`, `k-means`, trees and pruning, `SVM`, `DBSCAN`, classification/regression metrics and `ROC-AUC`, regularization and kernels, `PCA`, ensembles (bagging/boosting/stacking), `EM`, bias-variance.
- [Введение в ML.ipynb](ML/Введение%20в%20ML.ipynb) — an interactive notebook for a quick start (pipelines and key metrics).

---

## Summary

This repository is my **portfolio set**:
- Algorithms — competitive and classic problems (Yandex + LeetCode).
- SQL — a full reference plus practice.
- Python libraries — NumPy, Matplotlib, Seaborn, Pandas.
- Econometrics — applied causal-inference projects.
- Finance — a full coursework project on investing.
- ML — a theory summary plus practical references and a notebook.

It shows the **breadth of my technical base** and the ability to apply these tools to practical cases.
