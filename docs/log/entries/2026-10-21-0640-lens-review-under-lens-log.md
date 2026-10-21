---
type: decision
module: lens-review
surfaces: [definition]
date: 2026-10-21T06:40
source_commits: {}
---

# lens-review declares its piece and comes under lens-log

## What was done
- Added `decomposition.json` (role `piece`) with surfaces: source (both PROVES repos, read or
  write), identity (`CHARTER.md`, `CLAUDE.md`, `docs/BUILD.md`), definition, skills, module
  (`src/**`).
- Enabled `lens-log@lizo-skills` (0.1.3) in `.claude/settings.json` and added this log folder.
- Done from the lens-core session as Phase 0 of the approved roadmap method
  (lens-core `docs/plans/2026-10-21-roadmap-method-proposal.md`).

## What was found / decided
This is wiring only, not a spec for what lens-review builds. The sources list is the conservative
default; narrow it to the PROVES paths this module actually works once the source has been
worked. Progress now goes in this folder as log entries, and lens-log enforces it per turn.

## Lessons
Without a declared piece, a repo's work leaves no record; wire logging before building.
