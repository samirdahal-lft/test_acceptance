---
approved_by: "samir dahal"
approved_at: "2026-10-01"
planned_behaviors: "3"
approved_sha256: "ff882996ec12d13427ed1fdc2d413d4c7fe083ca1b64c941d821c5f9ad98090f"
---
## Exec Plan — Task T-streamlit-greeter-4mm918

**Will build:**
- B-1: `greeting(name)` pure function returns "Good day, <name>" for non-empty name (AC-1)
- B-2: `greeting(name)` returns `None` (or empty string) for empty/whitespace-only name (AC-2)
- B-3: `app.py` Streamlit page — text input renders greeting via `greeting()` when name is non-empty (AC-3, e2e)

**Approach:**
- Extract a pure `greeting(name: str) -> str | None` function so unit tests can exercise it without Streamlit
- `app.py` calls `greeting()` and conditionally calls `st.write()` on the result
- Tests for B-1 and B-2 are plain pytest unit tests against `greeting()`; B-3 is a smoke integration test using `streamlit.testing.v1.AppTest`

**Boundaries & mocks:**
- No external boundaries (no network, no DB, no filesystem I/O at runtime)
- No fakes required; all tests are pure Python unit/integration tests

**Behaviors (TDD order):**
- B-1 (tracer bullet): `greeting("Alice")` → `"Good day, Alice"` — proves the happy path
- B-2: `greeting("")` → no greeting; `greeting("   ")` → no greeting — proves the empty/whitespace guard
- B-3: Streamlit app renders "Good day, Alice" when name input is "Alice"; renders nothing when input is empty

**PR will contain:**
- `app.py` — Streamlit single-page app with `greeting()` helper and conditional `st.write()`
- `tests/T-streamlit-greeter-4mm918/test_greeting.py` — unit + AppTest smoke tests

**Open questions / ambiguities:** None — scope is fully defined by the TSD snapshot.

**Path:** L (lean)
**Escalation signals hit:** 0
- [ ] Refactor pass done (on green; tests unchanged) — before PR
