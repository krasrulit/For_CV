
# ML

В этом разделе — три собранных PDF-файла по **Machine Learning** и один ноутбук:

- [**ML_Практическая_справка.pdf**](./ML_Практическая_справка.pdf) — первая часть моего разбора по применению ML:  подготовка данных в `pandas/NumPy` (масштабирование `StandardScaler/MinMaxScaler`, кодирование `OneHotEncoder`); разбиение и валидация (`train_test_split`, `KFold/StratifiedKFold`, `cross_val_score`); пайплайны `Pipeline/ColumnTransformer` без data leakage; бейзлайны и метрики (`accuracy/precision/recall/F1`, `ROC-AUC`, `MSE/MAE/R²`); тюнинг (`GridSearchCV/RandomizedSearchCV`, `random_state`); нюансы дисбаланса (`class_weight`, стратификация).

- [**ML_Практическая_справка_2.pdf**](./ML_Практическая_справка_2.pdf) — продолжение разбора: `DBSCAN` (включая k-distance plot, `cosine`/`haversine`), метрики качества кластеризации (силуэт, индекс Данна), базовые регрессии (`OLS/Ridge/Lasso/Logistic`), `PCA`, ансамбли (`RandomForest`, `CatBoost/XGBoost/LightGBM`), blending/stacking и небольшие практические советы.

- [**ML_Теория.pdf**](./ML_Теория.pdf) — теоретический конспект: переобучение и кросс-валидация; `GD/SGD` и метод Ньютона; `kNN`; `k-means`; решающие деревья и pruning; `SVM`; `DBSCAN`; критерии качества кластеризации; метрики классификации/регрессии и `ROC-AUC`; регуляризация; ядра; `PCA` и выбор числа компонент; ансамбли (bagging/boosting/stacking); `EM`-алгоритм и разложение bias-variance.

- [**Введение в ML.ipynb**](./Введение%20в%20ML.ipynb) — первая лабораторная работа из учебника Яндекса по ML (первые эксперименты, базовые пайплайны и метрики).

---

## Навыки, которые демонстрирую

- Предобработка и оценивание: масштабирование/нормализация, разбиение на train/test, кросс-валидация, отбор компонент (`PCA`), ранняя остановка и регуляризация.  
- Линейные модели и их настройка: `LinearRegression`, `Ridge`, `Lasso`, `LogisticRegression` (пайплайны, ключевые гиперпараметры, интерпретация метрик).  
- Кластеризация и её оценка: `k-means`, `DBSCAN` (подбор `eps` по k-distance, `cosine` + `normalize`, `haversine` для геоданных), силуэт, индекс Данна, compactness/separation.  
- Деревья и ансамбли: `DecisionTree`, `RandomForest`, градиентный бустинг (`CatBoost`, `XGBoost`, `LightGBM`), blending и `StackingClassifier/StackingRegressor`.  
- Метрические методы и ядра: `kNN`, `SVM`, выбор и применение ядер.  
- Метрики: для классификации (`Accuracy`, `LogLoss`, `ROC-AUC`, `F1`) и регрессии (`MSE`, `MAE`, `R²`).

---

## Как читать

- **Практическая справка» (часть 1)** → [ML_Практическая_справка.pdf](./ML_Практическая_справка.pdf). 
- **Практическая справка (часть 2)** → [ML_Практическая_справка_2.pdf](./ML_Практическая_справка_2.pdf).   
- **Теоретическое обоснование и формулы** → [ML_Теория.pdf](./ML_Теория.pdf).  
- **Хочется «пощупать» вживую** → [Введение в ML.ipynb](./Введение%20в%20ML.ipynb) (запустить и повторить примеры).

> **Примечание.** Часть теоретических материалов взята из учебника преподавателя по ML в МГУ Антона Игоревича Андрейцева: [andreitsev/Machine-Learning-EF-MSU](https://github.com/andreitsev/Machine-Learning-EF-MSU).
