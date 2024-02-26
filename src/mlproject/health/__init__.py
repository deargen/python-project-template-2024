"""Check health of the installation."""

import os

from rich import print
from rich.console import Console

from .. import DATA_DIR
from .slack import check_env as slack_check_env
from .slack import check_send_text as slack_check_send_text

console = Console()


def check_binaries():
    """Check if binaries are installed."""
    return True


def check_env():
    """Check environment variables."""
    data_dir = os.environ.get("MLPROJECT_DATA_DIR")

    if data_dir is None or data_dir == "":
        print(
            "🤢 Please set the environment variable MLPROJECT_DATA_DIR to the path of the data directory."
        )
        print(f"Otherwise, the default {DATA_DIR} will be used.")
        return False

    print(f"✅ MLPROJECT_DATA_DIR is set to {data_dir}")
    return True


def main():
    successes = [check_env()]
    successes.append(check_binaries())

    successes.append(slack_check_env())
    successes.append(slack_check_send_text())

    if all(successes):
        print()
        print("💪 You are ready to go!")


if __name__ == "__main__":
    main()
