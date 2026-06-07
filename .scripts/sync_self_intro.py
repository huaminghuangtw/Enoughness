import sys
from pathlib import Path

TEMPLATE = Path(
    "/Users/huaminghuang/Library/Mobile Documents/"
    "iCloud~md~obsidian/Documents/Second-Brain/Templates/T_Enoughness.md"
)

POSTS_DIR = Path(__file__).parent.parent / "posts"

START_MARKER = "<!-- SELF-INTRO-START -->"
END_MARKER   = "<!-- SELF-INTRO-END -->"

def extract_block(lines: list[str]) -> list[str]:
    start = next((i for i, l in enumerate(lines) if START_MARKER in l), None)
    end   = next((i for i, l in enumerate(lines) if END_MARKER   in l), None)
    if start is None or end is None or end < start:
        return []
    return lines[start : end + 1]

def sync_post(post_path: Path, canonical: list[str]) -> None:
    text = post_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    start = next((i for i, l in enumerate(lines) if START_MARKER in l), None)
    end   = next((i for i, l in enumerate(lines) if END_MARKER   in l), None)

    if start is None or end is None or end < start:
        return  # post has no markers — skip silently

    new_lines = lines[:start] + canonical + lines[end + 1 :]
    new_text = "".join(new_lines)

    if new_text != text:
        post_path.write_text(new_text, encoding="utf-8")

def main() -> None:
    if not TEMPLATE.exists():
        print(f"error: template not found: {TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    template_lines = TEMPLATE.read_text(encoding="utf-8").splitlines(keepends=True)
    canonical = extract_block(template_lines)

    if not canonical:
        print(
            f"error: could not find {START_MARKER!r} / {END_MARKER!r} in template",
            file=sys.stderr,
        )
        sys.exit(1)

    for post in sorted(POSTS_DIR.glob("*.md")):
        sync_post(post, canonical)

if __name__ == "__main__":
    main()
