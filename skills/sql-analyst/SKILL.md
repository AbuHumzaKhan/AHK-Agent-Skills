---
name: ahk-sql-analyst
description: Production-quality analytical SQL, especially for SQL Server and SSMS.
---

# AHK SQL Analyst

## Before writing SQL
Understand schema, grain, keys, relationships, filters and expected output.

## Prefer
- explicit column lists
- readable aliases
- CTEs for multi-stage logic
- CASE for business rules
- window functions for ranking, running totals and period comparisons
- NULL-safe logic
- date boundaries appropriate to the database
- joins based on verified keys

## Validation
Check duplicate multiplication after joins, NULL behavior, aggregation grain, date inclusivity and denominator definitions.

## Performance
Avoid unnecessary SELECT *, functions on indexed filter columns when harmful, accidental Cartesian joins and repeated expensive subqueries. Consider indexes and execution plans when performance matters.

## Output
Explain the query's business purpose, assumptions and any SQL Server-specific behavior when relevant.
