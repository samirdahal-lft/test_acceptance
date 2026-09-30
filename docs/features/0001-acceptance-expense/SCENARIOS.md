---
approved_by: ""
approved_at: ""
---
# Scenarios 0001 — <feature under test>
> QA's first stamp: WHAT will be accepted, fixed before any test exists. Every scenario comes
> from the developer feature's approved (frozen) spec — never from what the code happens to do.
> One `lane approve` covers the scenarios, their test cases and the e2e plan below, and this
> kind's one task is created with it. Editing this file after the stamp reopens it.

**Frozen spec:** <path of the developer feature's approved spec document>
**Spec stamp:** <its approved_sha256 — the version these scenarios were written against>

## Scenarios
> One per rule of the frozen spec a user can observe, each with its test case.
- SC-1 <scenario> — rule: <spec section or AC> — steps: <what to do> — expected: <what must be seen>

## Execution Plan
> Approved BY this document's stamp: `lane start` copies this section verbatim into the
> worktree's exec-plan.md and carries your stamp onto it — no separate plan gate.

**Will build:** <the e2e tests, one per scenario: SC-1 …>
**Harness:** <cypress | playwright — and where the tests live>
