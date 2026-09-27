# lens-review

**The Lens — review: human accept/reject/edit of candidates; promote to the verified library.**

The Lens is a neutral, reusable "lab-in-a-box" for **systems discovery**: you launch a
*lab* (a systems observatory) that reads a system's artifacts, stages candidate
findings, has a human verify them, and serves a verified knowledge library.

`lens-review` is the **review** module — the "humans establish truth" step. It
presents staged candidates to a human who accepts/rejects/edits, records every
action in `decisions`, and promotes accepted candidates into `verified`.

## Where it sits

| Module | Role |
|---|---|
| **lens-core** | the standard + composition + launcher |
| **lens-ingest** | source material → staged candidate records |
| **lens-review** (here) | human accept/reject/edit → promote to the verified library |
| **lens-serve** | query the verified library (API + MCP) |
| **lens-observe** | signals over activity (active / orphaned / degrading / blind) |

The shared database shape (`candidates → decisions → verified`, plus lineage and
oversight) is defined in **lens-core**. This module reads/writes it over an
**injected** connection (`LENS_DB_URL`) — never hardcoded.

## Launch (stub)

```bash
pip install lens-review        # once published
lens-review --help
```

Connection is **injected** (`LENS_DB_URL` in your environment) — never hardcoded.
See [`.env.example`](.env.example).

## Identity

This repo has a [`CHARTER.md`](CHARTER.md) — its core directive and its boundary
within The Lens. Read it first. Precedent (how PROVES/Tapestry did it before) is
*guidance*, not this repo's identity.

## Status

Scaffold, 2026-09-26. Neutral/open. No proprietary source data.

## The Lens — related repositories

Part of **The Lens** — a modular, nearly-decomposable kit for systems discovery. Each repo stands on its own; together they compose a lab (a systems observatory).

- [lens-core](https://github.com/Lizo-RoadTown/lens-core) — main lab repo: shared standard + composition + launcher + the decomposition method
- [lens-ingest](https://github.com/Lizo-RoadTown/lens-ingest) — intake: source material into staged candidate records
- [lens-review](https://github.com/Lizo-RoadTown/lens-review) — review: human accept/reject/edit; promote to the verified library  **(this repo)**
- [lens-serve](https://github.com/Lizo-RoadTown/lens-serve) — serve: query the verified library (API + MCP)
- [lens-observe](https://github.com/Lizo-RoadTown/lens-observe) — observe: signals over activity (active / orphaned / degrading / blind)
