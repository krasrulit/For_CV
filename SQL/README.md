# SQL

This section has two compiled PDFs on **SQL (MySQL 8+)**:

- [**Функции_SQL.pdf**](./Функции_SQL.pdf) — my own SQL reference.
  It's essentially a condensed write-up of everything I know:
  filtering and aggregation, `JOIN`, subqueries and `UNION`, dates/strings/regex, `@` variables, `CTE (WITH)`, and window functions (`OVER()`), plus tricks like "FULL OUTER JOIN via UNION".

- [**Примеры_запросов.pdf**](./Примеры_запросов.pdf) — a set of SQL problems I wrote, with solutions and short explanations.
  Each problem is laid out as:
  **Database → Task → Solution → Explanation**.

---

## Skills demonstrated

- Aggregations (`SUM/COUNT/MIN/MAX`), `GROUP BY/HAVING`, filtering, and sorting.
- Joins: `INNER/LEFT/RIGHT JOIN`, `USING` vs `ON`, multi-step `JOIN`s in `SELECT/UPDATE/DELETE`.
- Subqueries and `UNION/UNION ALL`; emulating `FULL OUTER JOIN` in MySQL.
- Strings and dates: `SUBSTR/INSTR/CONCAT/REGEXP`, `FROM_UNIXTIME`, `DATEDIFF`, `MONTHNAME`, etc.
- `CTE (WITH)` and window functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `OVER()` aggregates).
- Mini-ETL: creating intermediate tables with `CREATE TABLE … AS`, computing metrics, and updates with subqueries.

---

## Task map (for [Примеры_запросов.pdf](./Примеры_запросов.pdf))

| #  | In brief                                  | Key techniques                                               |
|----|-------------------------------------------|--------------------------------------------------------------|
| 1  | Top genres by count                       | `JOIN`, `GROUP BY`, `SUM`, `HAVING`                          |
| 2  | Monthly revenue (2 years)                 | `UNION ALL`, `YEAR`, `MONTHNAME`, grouping by date          |
| 3  | Students with the top score               | subquery, `ORDER BY ... DESC LIMIT 1`, `DISTINCT`           |
| 4  | Question success rate                     | `LEFT JOIN`, share `SUM(is_correct)/COUNT`, `ROUND`, `SUBSTR` |
| 5  | `applicant` table                         | `CREATE TABLE … AS`, `LEFT JOIN`, summing by subject        |
| 6  | Removing those below thresholds           | `DELETE … USING … JOIN`, comparing `result` vs `min_result` |
| 7  | Awarding bonuses                          | `UPDATE` with a subquery, `IFNULL/IF`, `LEFT JOIN`          |
| 8  | Filling `step_keyword`                    | `INSERT … SELECT`, `JOIN`, `INSTR` (word search)            |
| 9  | Groups by number of solved steps          | nested aggregations, `COUNT(DISTINCT)`, `CASE`              |
| 10 | Step success rate (0% / 100%)             | 2 `CTE`s, `LEFT/RIGHT JOIN` + `UNION`, `IFNULL`             |
| 11 | Progress and certificates                 | `@step_count` variable, `COUNT(DISTINCT)`, `CASE`          |
| 12 | Average lesson time                       | 3 `CTE`s, `> 4h` filter, seconds → hours, `ROW_NUMBER`     |
| 13 | Relative ranking within a module          | `MAX() OVER (PARTITION BY)`, percentages, sorting          |
| 14 | Attempt breakdown for `student_59`        | `CTE`, `DENSE_RANK`, replacing "long" attempts, `SEC_TO_TIME` |
| 15 | Behavior groups (I/II/III), 2 variants    | Variant 1: `CTE+LEAD`; Variant 2: `CTE+LAG`                |

---

## How to read

- **Quick syntax refresher** — [Функции_SQL.pdf](./Функции_SQL.pdf) (table of contents + examples).
- **Practice-oriented cases** — [Примеры_запросов.pdf](./Примеры_запросов.pdf) (each case is self-contained: schema, query, explanation).
