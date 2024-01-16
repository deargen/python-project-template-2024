"""
Automatically generate __init__.py files for all subdirectories.
Useful before building mkdocs documentation.
"""

import os
from pathlib import Path


def gen_init_py(path):
    """Generate __init__.py files for all subdirectories of path"""
    for root, _, files in os.walk(path):
        if "__init__.py" in files:
            continue
        if root == path:
            continue
        if "__pycache__" in root:
            continue
        if root.endswith(".egg-info"):
            continue
        if root.endswith("src/ppmi/masif/data_pipe/data_list"):
            continue
        if root == str(SRC_DIR):
            continue

        with open(os.path.join(root, "__init__.py"), "w") as f:
            print("Generating __init__.py in", root)
            f.write("")


if __name__ == "__main__":
    SRC_DIR = Path(__file__).parent.parent / "src"
    gen_init_py(SRC_DIR)
