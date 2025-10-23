import re
from pathlib import Path

TEMPLATE_PATH = Path("/Users/huaminghuang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second-Brain/Templates/T_Enoughness.md")

POSTS_DIR = Path(__file__).parent.parent / "posts"

START_TAG = "<!-- SELF-INTRO-START -->"
END_TAG = "<!-- SELF-INTRO-END -->"

def extract_self_intro():
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    m = re.search(rf"{re.escape(START_TAG)}([\s\S]*?){re.escape(END_TAG)}", text)
    if not m:
        raise RuntimeError("Self-intro section not found in template.")
    return m.group(1).strip()


def update_post_file(post_file, self_intro):
    content = post_file.read_text(encoding="utf-8")
    new_content = re.sub(
        rf"{START_TAG}[\s\S]*?{END_TAG}",
        f"{START_TAG}\n{self_intro}\n{END_TAG}",
        content,
    )
    post_file.write_text(new_content, encoding="utf-8")

def main():
    self_intro = extract_self_intro()
    for post_file in POSTS_DIR.glob("*.md"):
        update_post_file(post_file, self_intro)

if __name__ == "__main__":
    main()
