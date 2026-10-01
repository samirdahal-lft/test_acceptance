## TSD S-0001.01 — Name input and greeting display  (PRD §S-0001.01)
| Aspect | Spec |
|--------|------|
| Interfaces | Single-page web UI: one text input control labelled for name entry; one text output area that conditionally renders a greeting |
| Data / State | No persistent state. In-session only: the current value of the name input (a string, held by the UI framework's re-render cycle) |
| Behavior | When the name input contains a non-empty string `name`, the output area renders the greeting `"Good day, {name}"`. When the name input is empty or whitespace-only, no greeting is rendered. |
| Access | Any user who can reach the running app in a browser. No authentication. |
| Boundaries | None — no external services, filesystem I/O, network calls, or clock access |
| Tests | unit: verify greeting string logic (non-empty name → correct greeting; empty/whitespace → no greeting); integration: N/A (no external boundaries); smoke: manual browser check that typing a name produces the greeting in the running app |
