"""Check health of the installation."""

import logging
import os

from ml_project import APP_NAME_UPPER, DATA_DIR

logger = logging.getLogger(__name__)


def check_binaries():
    """Check if binaries are installed."""
    return True


def check_env():
    """Check environment variables."""
    data_dir_env = os.environ.get(f"{APP_NAME_UPPER}_DATA_DIR")

    if data_dir_env is None or data_dir_env == "":
        logger.warning(
            f"🤒 Please set the environment variable {APP_NAME_UPPER}_DATA_DIR to the path of the data directory.\n"
            f"Otherwise, the default {DATA_DIR} will be used."
        )
        return False

    logger.info(f"✅ {APP_NAME_UPPER}_DATA_DIR is set to {data_dir_env}")
    return True


def main():
    successes = [check_env()]
    successes.append(check_binaries())

    if all(successes):
        logger.info("")
        logger.info("💪 You are ready to go!")


if __name__ == "__main__":
    main()
