# AHK-Agent-Skills

Reusable AI Agent Skills for Data Analytics, Business Analysis, Web Development, Learning Systems, and AI Agent Engineering.

## Included skills

| Skill | Purpose |
|---|---|
| data-analyst | End-to-end business and data analysis |
| data-cleaning | Profiling, cleaning and validation |
| sql-analyst | SQL Server analytics and query engineering |
| excel-analyst | Excel, Power Query, PivotTables and reporting |
| python-eda | Reproducible pandas/NumPy EDA |
| data-visualization | Decision-oriented charts and dashboards |
| business-analyst | Business analysis, KPIs and recommendations |
| requirements-engineering | Requirements and acceptance criteria |
| frontend-engineer | Production frontend engineering |
| react-engineer | React architecture and implementation |
| ui-ux-engineer | Information architecture and interaction design |
| web-motion | Accessible, performant web motion |
| debugging | Systematic root-cause debugging |
| testing-qa | Functional, data and regression testing |
| github-engineer | Repository and GitHub workflow |
| learning-architect | Progressive practical curriculum design |
| ai-agent-engineer | AI agent architecture and guardrails |

## Repository structure

```
AHK-Agent-Skills/
├── README.md
├── SKILLS.md
├── skills/
│   └── <skill-name>/SKILL.md
└── scripts/
    └── validate-skills.py
```

## Design principles

1. Understand the objective before choosing an implementation.
2. Inspect existing architecture, data and constraints before changing anything.
3. Prefer minimal, reversible and maintainable changes.
4. Make assumptions explicit.
5. Validate calculations, implementation and critical user flows.
6. Never fabricate data, tool output, test results or completion status.
7. Protect secrets and sensitive information.
8. Optimize for production usefulness rather than a plausible demo.

## Validation

Run:

```bash
python scripts/validate-skills.py
```

The validator checks that every skill has a `SKILL.md`, valid frontmatter, a matching skill name and a description.
