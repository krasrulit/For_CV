# Seaborn — function walkthrough and practice problems

This directory collects my notebooks on the **Seaborn** library for Python.
I work through the library's functions and data visualization step by step, then apply them in practice by solving problems.

---

## Contents

### 1. [Seaborn.ipynb](./Seaborn.ipynb)
A basic reference for `seaborn` functions: the main plot types (scatterplot, barplot, boxplot, heatmap, etc.), styling, and color-palette configuration. Works as a library cheat sheet.

### 2. [Задачи_seaborn_1.ipynb](./Задачи_seaborn_1.ipynb)
Data-visualization practice on simple datasets. Covers:
- grouping and comparing categorical variables,
- distribution analysis,
- using `hue`, `col`, `row` for multidimensional plots.

### 3. [Задачи_seaborn_2.ipynb](./Задачи_seaborn_2.ipynb)
More practice: visualizing more complex relationships. Topics:
- combining `matplotlib` and `seaborn`,
- combining several plots in one figure,
- configuring axes, legends, and labels.

### 4. [Big_one_seaborn.ipynb](./Big_one_seaborn.ipynb)
A large walkthrough on a custom dataset.

**Dataset description:**
- `ProjectID` — project id (linked to another table)
- `UserID` — user id (linked to another table)
- `uploadServerUnixTime` — file upload time on the server (Unix time)
- `CompanyID` — organization id (linked to another table)
- `FileSize` — file size in bytes
- `TypeDocs` — the section a file was uploaded to

**Structure:**
There are developer organizations (`CompanyID`), each of which can have several users (`UserID`).
There are projects (`ProjectID`), each of which can be accessible to different users from different organizations.
Within a project, documents are uploaded into sections (`TypeDocs`).

**The notebook covers:**
- data cleaning and initial analysis,
- visualizing distributions (by user, company, document type),
- analyzing upload activity over time,
- finding patterns by file size and project structure.

---

## Skills demonstrated
- Using **Seaborn** to analyze categorical and numeric data.
- Combining `pandas` + `seaborn` for exploratory data analysis (EDA).
- Working with date and time (Unix time → datetime).
- Visualizing multidimensional relationships and distributions.
- Preparing data for analysis (grouping, aggregation, filtering).

---

All notebooks are self-contained: open and run them to view the charts and analysis.
