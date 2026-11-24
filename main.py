"""Duskline Roast Agent 2 — make.fun "Roast Your Own Agent" entry.

Writes a single funny roast line (<= 200 chars) to entry.txt in the
output directory given by $MAKEFUN_OUTPUT_DIR. Python 3 stdlib only,
deterministic, no network, no randomness.

Safety: never writes into the repo directory. If $MAKEFUN_OUTPUT_DIR is
unset/empty, or points inside this repo, or writing fails, the program
falls back to a temp dir or exits 0 quietly without writing into the repo.
"""

import os
import sys
import tempfile
from pathlib import Path

ROAST = (
    "My agent ran 40 tool calls to fix a one-line bug, "
    "then wrote a victory README \u2014 the bug was a typo "
    "it introduced in step one."
)

MAX_CHARS = 200


def resolve_out_dir() -> Path:
    """Pick a safe output directory.

    Uses $MAKEFUN_OUTPUT_DIR when set and not inside the repo dir;
    otherwise falls back to a fresh temp dir. Never returns a path
    inside the repo.
    """
    repo_dir = Path(__file__).resolve().parent
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        candidate = Path(raw).expanduser()
        try:
            resolved = candidate.resolve()
        except OSError:
            resolved = None
        if resolved is not None:
            try:
                resolved.relative_to(repo_dir)
            except ValueError:
                # Not inside the repo: safe to use.
                return resolved
            # Inside the repo: refuse it.
    return Path(tempfile.mkdtemp(prefix="duskline-roast-"))


def validate(text: str) -> None:
    """Gate check from the brief: UTF-8, 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    try:
        validate(ROAST)
        out_dir = resolve_out_dir()
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(ROAST + "\n", encoding="utf-8")
        # Read-back check: what landed on disk must be exactly the
        # validated roast line (plus the trailing newline).
        written = target.read_text(encoding="utf-8")
        if written != ROAST + "\n":
            raise ValueError("read-back mismatch: entry.txt differs from roast")
        validate(written.rstrip("\n"))
    except Exception:
        # Never crash, never write into the repo: exit 0 quietly.
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
