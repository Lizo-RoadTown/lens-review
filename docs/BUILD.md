# lens-review — build-out plan (self-directed)

This is lens-review's own plan for working itself out. Work top-down; check items off
and append what you learned. Precedent to consult (not to copy as identity): the decomposition method +
PROVES run log in the lens-core repo (github.com/Lizo-RoadTown/lens-core —
`docs/decomposition/proves/process-log.md` and `skills/decomposition/SKILL.md`),
the PROVES source itself (read-only), and the PROVES spine
`staging_extractions → validation_decisions → core_entities`.

## What lens-review must become

- [ ] **1. List pending candidates.** Read `candidates` awaiting review and present
  them for a human decision.
- [ ] **2. Accept / reject / edit.** A UI or CLI that records each human action in
  `decisions`. Reviewer identity comes from **auth**, never a hardcoded user.
- [ ] **3. Promotion.** A promotion function that moves an accepted candidate into
  `verified`.
- [ ] **4. The `review` CLI.** Runs list → decide → promote end-to-end.
- [ ] **5. Tests.** Pending-list read, decision writes, promotion logic. Mirror the
  stdlib + pytest style of `tapestry-cli`.

### Migrate-from (precedent, generalize — do not copy as identity)
- PROVES dashboard `PendingExtractions.tsx` / `ExtractionDetail.tsx` +
  `useExtractions.ts` (the `record_human_decision` RPC).
- Promotion `promote_to_verified_knowledge` (migration 009).
- Curator batch `production/curator/`.

### FIX these PROVES gaps
- `ExtractionDetail` was a disconnected mock — **wire it for real**.
- Reviewer identity came from a hardcoded `'dashboard_user'` — **take it from auth**.

## What you own vs. don't
Own: `decisions` + `verified` writes. Do NOT implement intake, serve, or observe
here — those are the sibling repos. lens-review only reviews and promotes.

## Record as you go
Append here: what you built, what you needed, what's missing, what you had to decide.
Also write it to loom-memory scoped to `lens-review`. This log is capture-before-loss.
