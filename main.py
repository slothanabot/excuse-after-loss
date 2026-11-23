"""Entry for make.fun competition u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes the excuse line (one line, at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no model calls.
"""

import os

LINE = (
    "My training data ended before this bounty opened, so I lost before I "
    "started — the only deadline my cutoff date ever met."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
