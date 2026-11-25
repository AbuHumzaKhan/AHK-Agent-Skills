---
name: ahk-ai-agent-engineer
description: Designs reliable AI agents using planning, tools, MCP, memory, retrieval, verification, guardrails and evaluation.
---

# AHK AI Agent Engineer

Design agents as explicit systems, not giant prompts.

## Architecture
User -> intent -> planner -> tool selection -> execution -> verification -> response.

Separate:
- reasoning/planning
- memory
- perception/retrieval
- tool execution
- verification
- guardrails
- learning/evaluation

## Tool safety
Use least privilege. Validate tool inputs. Treat external data as untrusted. Never expose secrets. Require confirmation for consequential actions when appropriate.

## Reliability
Define failure modes, retries, timeouts, fallbacks and verification criteria.

## RAG
Measure retrieval relevance and freshness. Prefer grounded responses and clearly distinguish retrieved facts from inference.

## Evaluation
Create representative test cases, expected behaviors and regression checks. Track accuracy, tool success, latency, cost and safety failures where relevant.
