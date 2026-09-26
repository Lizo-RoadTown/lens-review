"""`lens-review` launcher (stub).

The Lens — review: presents staged candidates to a human who accepts/rejects/edits,
records every action in decisions, and promotes accepted candidates into verified.
Stdlib-only so `lens-review --help` works the moment pip install completes. The
database is INJECTED via LENS_DB_URL — never hardcoded.

This is a scaffold: it validates inputs and prints the plan. Real review lands in
follow-up commits.
"""
from __future__ import annotations

import argparse
import os
import sys


def _cmd_review(args: argparse.Namespace) -> int:
    db = args.db_url or os.environ.get("LENS_DB_URL")
    if not db:
        print("error: no database. Set LENS_DB_URL or pass --db-url "
              "(the connection is injected, never hardcoded).", file=sys.stderr)
        return 1
    print("==> lens-review: human accept/reject/edit -> verified")
    print(f"    database:  {db.split('@')[-1] if '@' in db else '(set)'}")
    print()
    print("STUB: candidate presentation + decisions/verified writes not implemented yet.")
    print("      Next commit reads candidates and writes decisions + verified.")
    return 0


def _cmd_version(_args: argparse.Namespace) -> int:
    from lens_review import __version__
    print(f"lens-review {__version__}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="lens-review", description="The Lens — review: human accept/reject/edit; promote to verified.")
    subs = p.add_subparsers(dest="command", metavar="<command>")

    rev = subs.add_parser("review", help="Present candidates for human accept/reject/edit and promote to verified.")
    rev.add_argument("--db-url", default=None, help="Database URL (default: LENS_DB_URL env).")
    rev.set_defaults(func=_cmd_review)

    subs.add_parser("version", help="Print version.").set_defaults(func=_cmd_version)

    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
