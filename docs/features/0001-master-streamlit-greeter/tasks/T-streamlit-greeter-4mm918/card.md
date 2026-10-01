---
approved_by: "samir dahal"
approved_at: "2026-10-01"
approved_sha256: "0383245b624539b6f7c4bf62ec250bb65140b328693da3241f2f935e1c474275"
---
## Task T-streamlit-greeter-4mm918 — Name input renders personalised greeting
**Parent:** story S-0001.01 · feature 0001 (docs/features/0001-master-streamlit-greeter/ — its BRIEFING.md + PRD.md + TSD.md)
**Slice:** complete vertical — text input + conditional greeting output + unit tests
**Acceptance criteria:**
- [ ] AC-1 [behavior]: When a non-empty name is entered, the greeting "Good day, <name>" is displayed
- [ ] AC-2 [behavior]: When the input is empty or whitespace-only, no greeting is displayed
- [ ] AC-3 [e2e]: A user opening the app in a browser can type a name and see the greeting on the same page
**End-to-end AC:** AC-3 [e2e] — reachable through the running app
**Tests:** AC-1, AC-2, AC-3
**Test scope:** tests/T-streamlit-greeter-4mm918/
**Done =** reviewable PR, all tests pass, links to chain. One PR per task.
