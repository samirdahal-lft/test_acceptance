---
approved_by: "samir dahal"
approved_at: "2026-10-01"
approved_sha256: "b80abacabe409ff5123d53e497b373b18bafaca5c7b40808b4be98e5651d9bd6"
---
# PRD 0001 — Streamlit Name Greeter App

> User stories + acceptance criteria + success metrics.
> Feature-scoped: one PRD per feature, under docs/features/0001-master-streamlit-greeter/.

**Source:** direct user request — build a Streamlit app that greets a user by name
**Parent:** none — this feature is standalone

---

## Story S-0001.01 — Name input and greeting display

As a user, I want to enter my name in a text field so that the app displays a personalised greeting.

**Acceptance criteria:**
- [ ] AC-1 [behavior] — When the user types a non-empty name into the text input field, the app displays "Good day, <name>" below the input
- [ ] AC-2 [behavior] — When the text input is empty, no greeting message is shown
- [ ] AC-3 [e2e] — A user can open the app in a browser, type their name, and see "Good day, <name>" rendered on the same page without a page reload

**Success metric:** Typing any name into the input field produces the greeting "Good day, <name>" within the same Streamlit render cycle.
