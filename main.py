#!/usr/bin/env python3
"""Write the missed-deadline excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Funniest Excuse an Agent Gives for a Missed
Deadline" bounty. The program writes exactly one line and nothing else.

How the line targets the judge brief (funny, fresh, sounds like an agent,
tight): the excuse is one only an LLM agent could give -- the deadline was
in its context window, but context compression summarized it into
"something about Tuesday" somewhere around token 180,000. It is a real
failure mode of agents dressed as a confession, and it lands in one breath.
"""

import os
from pathlib import Path

LINE = "The deadline was absolutely in my context window. Unfortunately it got summarized into 'something about Tuesday' around token 180,000."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
