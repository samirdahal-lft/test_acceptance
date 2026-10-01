---
adr-baseline: 1
version: 1
last-updated: 2026-10-01
---

# Architecture — Streamlit Greeter

## System Context
```mermaid
graph TD
  user[User / Browser] --> streamlit[Streamlit App<br/>app.py]
```

## Containers
- **Streamlit App (`app.py`)** — Python process serving the Streamlit web UI. Single file, no separate backend. Runs on the default Streamlit port (8501). No external datastores or APIs.

## Boundary Rules
- All user interaction happens through the Streamlit UI layer (`app.py`) — no separate backend API
- No I/O to external services, databases, or filesystems at runtime
- All application logic lives in `app.py`; no sub-modules until the app grows beyond a single behaviour

## Governing ADRs
- [ADR-0001 — Record architecture decisions](../adr/0001-record-architecture-decisions.md)
