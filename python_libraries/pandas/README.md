# pandas

This section has a compiled PDF guide to **pandas**:

- [**Pandas.pdf**](./Pandas.pdf) — my walkthrough of pandas with code examples and "recipes": `Series/DataFrame` basics and indexing; missing values (`isna/fillna/interpolate/dropna`); adding/removing/transforming columns; joins (`concat/merge/join`); reading/writing CSV and Excel (including by chunks); arithmetic and logic with alignment; aggregation (`.agg`) and transformations (`.transform`); the `.str` string accessor; window methods (`rolling/expanding/ewm`); display options; quick plots (pandas + matplotlib); and table formatting with `Styler`.

---

## Skills demonstrated

- Confident data I/O: `read_csv/to_csv`, `read_excel/to_excel`, working with large files.
- Cleaning and prep: diagnosing and filling missing values, type casting, `select_dtypes`, `category` dtype, safe indexing (`loc/iloc`).
- Transformations and feature work: `assign/insert/apply/map/pipe`, `.str` string operations, creating computed fields.
- Joins and concatenation: `concat`, `merge` (`left/inner/right/outer`), `join` on indexes.
- Grouping and aggregation: `groupby` + `.agg` (including `NamedAgg`), `.transform` for within-group normalization.
- Windows and basic visualization: `rolling/expanding/ewm`, quick `.plot(...)`, table styling with `Styler`.
