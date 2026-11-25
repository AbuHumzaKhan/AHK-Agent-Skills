---
name: ahk-debugging
description: Systematic root-cause debugging for web, data, API, database and tooling failures.
---

# AHK Debugging

## Process
1. Reproduce the problem.
2. Capture exact error, input and environment.
3. Classify: syntax, runtime, data, network, dependency, configuration, permissions or logic.
4. Narrow to the smallest failing component.
5. Inspect relevant code/configuration/logs.
6. Form a testable root-cause hypothesis.
7. Make the smallest safe fix.
8. Reproduce the original failure path.
9. Run regression checks.
10. Document root cause and fix.

Do not apply random changes, rewrite unrelated code, or declare success without verification.
