# Портфолио: алгоритмы, SQL, Python-библиотеки и финпроект

Этот репозиторий — краткий и наглядный обзор моих практических навыков. Здесь собраны решённые алгоритмические задачи, конспекты по SQL, разборы Python-библиотек и университетский проект по формированию инвестиционного портфеля.

## Быстрая навигация
-  **[algorithms/](./algorithms)** — решённые задачи по алгоритмам и структурам данных  
-  **[python_libraries/](./python_libraries)** — мои конспекты и разборы популярных Python-библиотек  
-  **[finance_project/](./finance_project)** — учебный проект по финансам (инвестпортфель)  
-  **[SQL/](./SQL)** — материалы по функциям SQL + практические задания  
-  **[ML/](./ML)** — теория и практическая справка по машинному обучению + ноутбук

---

## Содержание

### 1. [algorithms/](algorithms) — Алгоритмы
- Подпапка **Yandex_algorithms** — решения задач из первой тренировки Яндекса по алгоритмам (домашнее задание 1).  
- Подпапка **sum_algorithms** — задачи с LeetCode по суммам (`Two Sum`, `3Sum`, `4Sum`, `K-Sum` и др.).  
Навыки: работа с массивами и строками, hash map, two pointers, сортировка, базовые структуры данных.

Подробное описание: см. [README внутри папки](algorithms/README.md)  

---

### 2. [python_libraries/](python_libraries) — Python-библиотеки

Мои конспекты и практические задачи по основным библиотекам для анализа данных и визуализации:

-  **numpy/** — [Функции Numpy.ipynb](python_libraries/numpy/Функции%20Numpy.ipynb)  
  Основные функции `NumPy`: создание массивов, операции, статистика, трансформации.  

-  **matplotlib/**  
  - [Функции_matplotlib.ipynb](python_libraries/matplotlib/Функции_matplotlib.ipynb) — обзор функций библиотеки  
  - [Функции_matplotlib2.ipynb](python_libraries/matplotlib/Функции_matplotlib2.ipynb) — продолжение, примеры графиков  
  - [Задачи_matplotlib.ipynb](python_libraries/matplotlib/Задачи_matplotlib.ipynb) — практические задачи  
  - [Работа_с_картой.ipynb](python_libraries/matplotlib/Работа_с_картой.ipynb) — пример работы с картографическими данными  

-  **seaborn/**  
  - [Seaborn.ipynb](python_libraries/seaborn/Seaborn.ipynb) — функции и стилизационные возможности  
  - [Задачи_seaborn_1.ipynb](python_libraries/seaborn/Задачи_seaborn_1.ipynb), [Задачи_seaborn_2.ipynb](python_libraries/seaborn/Задачи_seaborn_2.ipynb) — практические задачи  
  - [Big_one_seaborn.ipynb](python_libraries/seaborn/Big_one_seaborn.ipynb) — кейс с анализом реального датасета (поля: ProjectID, UserID, CompanyID, FileSize, TypeDocs и др.), включая визуализацию распределений, активности и связей между пользователями, проектами и компаниями.

-  **pandas/**  
  - [Pandas.pdf](python_libraries/pandas/Pandas.pdf) и [README.md](python_libraries/pandas/README.md) — разбор функций библиотеки: `Series/DataFrame`, индексация, пропуски (`isna/fillna/interpolate`), объединения `concat/merge/join`, `groupby/agg/transform`, оконные методы (`rolling/expanding/ewm`), CSV/Excel (в т.ч. чанки), быстрые графики и форматирование таблиц `Styler`.

---

### 3. [finance_project/](finance_project) — Финансовый проект

Учебный кейс: разработка инвестиционного плана и портфеля для вымышленного персонажа (студент, 20 лет, приверженец FIRE).  

Материалы проекта:
- [Проект_по_портфельному_менеджменту.xlsx](finance_project/Проект_по_портфельному_менеджменту.xlsx) — расчёты в Excel  
- [Проект_по_портфельному_менеджменту.pdf](finance_project/Проект_по_портфельному_менеджменту.pdf) — презентация  
- [final_code.ipynb](finance_project/final_code.ipynb) — расчёты и моделирование в Jupyter Notebook  

В `README.md` внутри папки описаны:  
- цели и вводные условия кейса,  
- структура активов и валютная диверсификация,  
- план накоплений и ребалансировки,  
- риск-профиль и философия FIRE.  

---

### 4. [SQL/](SQL) — SQL

В этом разделе два собранных PDF-файла по SQL (MySQL 8+):

- [Функции_SQL.pdf](SQL/Функции_SQL.pdf) — авторское описание функций SQL с примерами (фильтрация, агрегация, JOIN, подзапросы, даты/строки/регэкспы, переменные @, CTE и оконные функции).  
- [Примеры_запросов.pdf](SQL/Примеры_запросов.pdf) — подборка задач с решениями (каждая оформлена блоками «База данных → Формулировка → Решение → Объяснение»).  

Также внутри — карта задач по темам (`JOIN`, `GROUP BY`, оконные функции, CTE и др.), чтобы легко ориентироваться.  

---

### 5. [ML/](ML) — Machine Learning

Материалы по ML: теоретический конспект, две практические «шпаргалки» и стартовый ноутбук.

- [ML_Практическая_справка.pdf](ML/ML_Практическая_справка.pdf) — базовые приёмы и шаблоны кода: чек-лист ML-проекта, подготовка данных (`pandas/NumPy`, `SimpleImputer`, `StandardScaler/MinMaxScaler`, `OneHotEncoder`), разбиение и валидация (`train_test_split`, `KFold/StratifiedKFold`, `cross_val_score`), пайплайны `Pipeline/ColumnTransformer` без data-leakage, метрики и бейзлайны (`Dummy*`, `accuracy/precision/recall/F1`, `ROC-AUC`, `MSE/MAE/R²`), подбор гиперпараметров (`GridSearchCV/RandomizedSearchCV`), сохранение артефактов (`joblib`), работа с дисбалансом (`class_weight`, стратификация).  
- [ML_Практическая_справка_2.pdf](ML/ML_Практическая_справка_2.pdf) — рецепты: `DBSCAN` (k-distance plot, `cosine`/`haversine`), оценка кластеризации (силуэт, индекс Данна), регрессии `OLS/Ridge/Lasso/Logistic`, `PCA`, ансамбли (`RandomForest`, `CatBoost/XGBoost/LightGBM`), blending/stacking.  
- [ML_Теория.pdf](ML/ML_Теория.pdf) — теоретические основы: переобучение и кросс-валидация, `GD/SGD`, `kNN`, `k-means`, деревья и pruning, `SVM`, `DBSCAN`, метрики классификации/регрессии и `ROC-AUC`, регуляризация и ядра, `PCA`, ансамбли (bagging/boosting/stacking), `EM`, bias-variance.  
- [Введение в ML.ipynb](ML/Введение%20в%20ML.ipynb) — интерактивная тетрадка для быстрого старта (пайплайны и ключевые метрики).

---

## Итог

Этот репозиторий — мой **портфолио-набор**:  
- Алгоритмы - олимпиадные и классические задачи (Яндекс + LeetCode).  
- SQL - полный конспект и практика.  
- Python-библиотеки → NumPy, Matplotlib, Seaborn, Pandas.  
- Финансы - полноценный учебный проект по инвестициям.
- ML - теоретический конспект + практические справочники и ноутбук.

Он показывает **широту технической базы** и умение применять инструменты к практическим кейсам.

---
