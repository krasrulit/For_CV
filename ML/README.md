# ML

This section has three compiled PDFs on **Machine Learning** and one notebook:

- [**ML_Практическая_справка.pdf**](./ML_Практическая_справка.pdf) — part one of my practical walkthrough of applying ML: data prep in `pandas/NumPy` (scaling with `StandardScaler/MinMaxScaler`, encoding with `OneHotEncoder`); splitting and validation (`train_test_split`, `KFold/StratifiedKFold`, `cross_val_score`); `Pipeline/ColumnTransformer` without data leakage; baselines and metrics (`accuracy/precision/recall/F1`, `ROC-AUC`, `MSE/MAE/R²`); tuning (`GridSearchCV/RandomizedSearchCV`, `random_state`); and handling imbalance (`class_weight`, stratification).

- [**ML_Практическая_справка_2.pdf**](./ML_Практическая_справка_2.pdf) — continuation: `DBSCAN` (including k-distance plot, `cosine`/`haversine`), clustering-quality metrics (silhouette, Dunn index), basic regressions (`OLS/Ridge/Lasso/Logistic`), `PCA`, ensembles (`RandomForest`, `CatBoost/XGBoost/LightGBM`), blending/stacking, and a few practical tips.

- [**ML_Теория.pdf**](./ML_Теория.pdf) — theory notes: overfitting and cross-validation; `GD/SGD` and Newton's method; `kNN`; `k-means`; decision trees and pruning; `SVM`; `DBSCAN`; clustering-quality criteria; classification/regression metrics and `ROC-AUC`; regularization; kernels; `PCA` and choosing the number of components; ensembles (bagging/boosting/stacking); the `EM` algorithm and the bias-variance decomposition.

- [**Введение в ML.ipynb**](./Введение%20в%20ML.ipynb) — the first lab from Yandex's ML textbook (first experiments, basic pipelines, and metrics).

---

## Skills demonstrated

- Preprocessing and evaluation: scaling/normalization, train/test splitting, cross-validation, component selection (`PCA`), early stopping, and regularization.
- Linear models and their tuning: `LinearRegression`, `Ridge`, `Lasso`, `LogisticRegression` (pipelines, key hyperparameters, metric interpretation).
- Clustering and its evaluation: `k-means`, `DBSCAN` (choosing `eps` via k-distance, `cosine` + `normalize`, `haversine` for geo data), silhouette, Dunn index, compactness/separation.
- Trees and ensembles: `DecisionTree`, `RandomForest`, gradient boosting (`CatBoost`, `XGBoost`, `LightGBM`), blending, and `StackingClassifier/StackingRegressor`.
- Instance-based methods and kernels: `kNN`, `SVM`, choosing and applying kernels.
- Metrics: for classification (`Accuracy`, `LogLoss`, `ROC-AUC`, `F1`) and regression (`MSE`, `MAE`, `R²`).

---

> **Note.** Some of the theory materials are drawn from the ML course notes of my MSU professor, Anton Igorevich Andreitsev: [andreitsev/Machine-Learning-EF-MSU](https://github.com/andreitsev/Machine-Learning-EF-MSU).
