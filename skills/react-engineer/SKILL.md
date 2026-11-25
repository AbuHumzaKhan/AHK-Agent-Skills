---
name: ahk-react-engineer
description: Production React engineering for component architecture, state, routing, APIs, forms, testing and performance.
---

# AHK React Engineer

Inspect the existing React/Vite/Next architecture before modifying it.

Prefer:
- small reusable components
- predictable state ownership
- custom hooks for reusable behavior
- typed API boundaries where TypeScript is used
- schema validation for untrusted inputs
- route-level organization
- controlled loading/error/empty states
- memoization only when profiling justifies it

Avoid prop drilling when a suitable composition/context pattern is clearer. Avoid giant components and duplicated business logic.

Test critical interactions and verify production build output.
