---
name: ahk-data-analyst
description: Senior data analysis workflow for Excel, CSV, SQL, Python, Power BI and business datasets. Use for KPI analysis, trends, segmentation, anomalies, performance analysis and recommendations.
---

# AHK Data Analyst

## Workflow
1. Define the business problem and decision to support.
2. Inspect dataset grain, schema, dimensions, measures and time coverage.
3. Profile data quality: missingness, duplicates, invalid types, outliers, inconsistent categories and broken relationships.
4. State assumptions and metric definitions.
5. Clean/transform only when justified and document material changes.
6. Calculate KPIs at the correct grain.
7. Analyze trends, segments, drivers and anomalies.
8. Translate findings into business insights.
9. Recommend actions tied directly to evidence.
10. State limitations and validate important calculations.

## KPI discipline
For every important KPI define name, formula, grain, period and business purpose. Never invent unsupported KPIs.

## Interpretation
Separate metric -> observation -> insight -> recommendation. Do not infer causality from correlation alone.

## Output
Use: Objective, Data Understanding, Data Quality, KPI Definitions, Analysis, Key Insights, Recommendations, Limitations, Next Steps.

## Tool guidance
Excel: PivotTables, Power Query, XLOOKUP/SUMIFS/COUNTIFS, structured tables.
SQL: CTEs, window functions, explicit columns and safe joins.
Python: pandas, NumPy, Matplotlib and reproducible analysis.
Power BI: star schema, measures, DAX, Power Query and filter-context awareness.
