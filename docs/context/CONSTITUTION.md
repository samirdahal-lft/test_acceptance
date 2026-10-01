# Engineering Constitution — Streamlit Greeter

> Human-maintained. Update when conventions change; review when onboarding.

## Stack
- Runtime: Python 3.x
- Language: Python
- Framework: Streamlit
- DB: none
- Test runner: pytest (inferred — no test runner committed yet; open question for first task)

## Conventions
1. Single entrypoint `app.py` at the repo root — NOT: split across multiple modules until scope demands it
2. Streamlit built-ins only (`st.text_input`, `st.write`, etc.) — NOT: raw HTML/CSS injection or custom components
3. Greeting logic is inline in `app.py` (no helper functions needed for this scope) — NOT: over-engineering a single conditional

## Hard Rules
- Never store user-entered names to disk, a database, or external service
- Never add dependencies beyond `streamlit` without an ADR

## File Organization
- `app.py` → Streamlit application entrypoint
- `docs/` → LANE artifacts (specs, tasks, context, ADRs)
- `requirements.txt` (or `pyproject.toml`) → Python dependencies (to be created on first task)

## Open questions (for human to resolve)
- Test runner: pytest assumed, but not yet confirmed by a committed `pyproject.toml` or `requirements-dev.txt`
- Dependency pinning: `requirements.txt` vs. `pyproject.toml` — decide on first task
