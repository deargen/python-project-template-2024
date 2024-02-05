"""
Get minimum python version from pyproject.toml.

Note:
    It only works if the format is like this: ">=3.11", ">=3.11,<3.12"
"""

from pathlib import Path

import toml

pyproject = toml.load(Path(__file__).parent.parent / "pyproject.toml")

version_range = pyproject["project"]["requires-python"]

# get minimum python version
# it has a format like this: ">=3.6", ">=3.7,<3.8"
min_version = version_range.split(",")[0].replace(">=", "")
print(min_version)  # noqa: T201
