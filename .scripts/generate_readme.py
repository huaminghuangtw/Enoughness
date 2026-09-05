#!/usr/bin/env python3

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE / "posts"
README = BASE / "README.md"

TEMPLATE = Path(
    "/Users/huaminghuang/Library/Mobile Documents/"
    "iCloud~md~obsidian/Documents/Second-Brain/Templates/T_Enoughness.md"
)

START_MARKER = "<!-- SELF-INTRO-START -->"
END_MARKER = "<!-- SELF-INTRO-END -->"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
ISSUE_RE = re.compile(r"^issue:\s*(\d+)\s*$", re.M)
TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
DRAFT_RE = re.compile(r"^draft:\s*true\s*$", re.M)


def read_self_intro() -> str:
    text = TEMPLATE.read_text(encoding="utf-8")
    m = re.search(
        rf"{re.escape(START_MARKER)}\s*(.*?)\s*{re.escape(END_MARKER)}",
        text,
        re.S,
    )
    return m.group(1).strip()


def parse_post(post: Path):
    text = post.read_text(encoding="utf-8")
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return None
    block = fm.group(1)
    issue = ISSUE_RE.search(block)
    title = TITLE_RE.search(block)
    if not issue or not title:
        return None
    return {
        "issue": int(issue.group(1)),
        "title": title.group(1).strip(),
        "draft": bool(DRAFT_RE.search(block)),
    }


def main() -> None:
    intro = read_self_intro()

    posts = []
    for post in sorted(POSTS_DIR.glob("enoughness-*.md")):
        meta = parse_post(post)
        if meta and not meta["draft"]:
            posts.append(meta)

    lines = [
        f"* #{p['issue']} [{p['title']}](https://huam.ing/enoughness-{p['issue']})"
        for p in sorted(posts, key=lambda p: p["issue"], reverse=True)
    ]

    content = (
        "# Enoughness\n\n"
        f"{intro}\n\n"
        + "\n".join(lines)
        + "\n"
    )

    README.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
