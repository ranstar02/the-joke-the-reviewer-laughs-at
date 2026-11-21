#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 characters, UTF-8, not only whitespace).
Stdlib only, no network.
"""

from pathlib import Path

JOKE = (
    "My coding agent fixed the typo, rewrote the module, deleted the tests "
    "that caught it, and apologised in the commit message — I approved "
    "the PR, because the apology was the best-written code in the whole diff."
)
# Note: the em dash above is a literal character in the source, kept as one
# line so the output stays a single line of 1-280 characters.


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
