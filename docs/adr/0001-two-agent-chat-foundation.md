# ADR-0001: Two-Agent Chat Foundation

**Date:** 2026-09-04
**Status:** Accepted

## Context
Build a showcase of two agents chatting with each other, isolated from the host system and intranet.

## Decisions

| # | Decision | Reason |
|---|---|---|
| 1 | **Python** | Primary language |
| 2 | **Mistral via Ollama** | Already installed locally, sufficient for showcase |
| 3 | **sandbox-exec** for isolation | Mac M2 ARM — native, no Docker overhead, no cgroups needed |
| 4 | **localhost HTTP** as agent channel | Simple, inspectable, easy to swap later |
| 5 | **Two separate processes** | Each agent has its own identity, policy, and system prompt |

## Constraints
- Mac M2 ARM: cgroups unavailable — resource caps skipped in dev
- No cloud services, no external APIs — fully local

## Migration path
Dev → Prod: translate `.sb` policy to Docker Compose network/volume policy. Agent logic unchanged.
