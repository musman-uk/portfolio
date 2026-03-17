import os
import shutil
import re

RENAME_MAP = {
    "independent-projects": "exploratory-projects",
    "behind-the-work": "behind-the-craft",
}

TITLE_MAP = {
    "Independent Projects": "Exploratory Projects",
    "Behind the Work": "Behind the Craft",
}

def apply_folder_renames():
    for old, new in RENAME_MAP.items():

        old_exists = os.path.exists(old)
        new_exists = os.path.exists(new)

        if not old_exists and new_exists:
            print(f"✓ {old} already renamed to {new}, skipping.")
            continue

        if not old_exists and not new_exists:
            print(f"⚠️ Neither {old} nor {new} exist, skipping.")
            continue

        if old_exists and not new_exists:
            print(f"Renaming {old} → {new}")
            shutil.move(old, new)
            update_markdown_links(old, new)
            continue

        if old_exists and new_exists:
            print(f"⚠️ Both {old} and {new} exist. Skipping to avoid data loss.")
            continue


def update_markdown_links(old, new):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                if old in content:
                    content = content.replace(old, new)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated links in {path}")


def update_titles():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                updated = False
                new_lines = []

                for line in lines:
                    stripped = line.strip()

                    for old, new in TITLE_MAP.items():

                        # Case 1: Heading with emoji or without, containing the old title
                        if stripped.startswith("#") and old in stripped:
                            line = line.replace(old, new)
                            updated = True

                        # Case 2: Plain-text section title (emoji allowed)
                        elif old in stripped and not stripped.startswith("#"):
                            # e.g. "🎨 Independent Projects"
                            line = line.replace(old, new)
                            updated = True

                    new_lines.append(line)

                if updated:
                    with open(path, "w", encoding="utf-8") as f:
                        f.writelines(new_lines)
                    print(f"Updated titles in {path}")


def validate_links():
    print("\nValidating links...")
    missing = False

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                links = re.findall(r'\(([^)]+)\)', content)

                for link in links:
                    if "://" in link:
                        continue

                    link_path = os.path.normpath(os.path.join(root, link))

                    if not os.path.exists(link_path):
                        missing = True
                        print(f"⚠️ Missing file referenced in {path}: {link}")

    if not missing:
        print("✓ No missing links found.")


if __name__ == "__main__":
    apply_folder_renames()
    update_titles()
    validate_links()
