"""Make the AI Judge Laugh — entry program.

Writes one joke about office life, a single line, to /output/entry.txt.
Deterministic: same bytes on every run.

The joke is a true office observation — every calendar has a "quick
sync" that never ends — with the laugh in the escalation at the end:
it has outlived two managers and one marriage.
"""

import os


ENTRY = "My calendar has a meeting called 'quick sync' that has outlived two managers and one marriage."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
