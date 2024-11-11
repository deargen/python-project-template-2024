r"""
Initialize dotenv configuration and common directories.

The package could be installed as develop mode (`pip install -e .`) or normally (`pip install .`),
so this module tries to support both cases.

This sets up the following variables:
- `default_log_level`: The default log level. (defaults to INFO)
    Can be configured with the environment variable `{app_name_upper}_LOG_LEVEL`.
- `PROJECT_DIR`: The project directory, or None.
    It is set to `None` if the package is NOT installed in development mode. (i.e., `pip install .`)
    We make it None to discourage the use of this path. Only use for development.
- `DATA_DIR`: The data directory, defaults to `{PROJECT_DIR}/data` or `~/.local/share/{app_name}`.
- `LOG_DIR`: `{DATA_DIR}/logs`.
- `APP_CONFIG_DIR`: The directory where the `.env` file is loaded from, or None.
- `__version__`: The version of the package.
- `app_name`: The name of the module. (alias of `__name__`) (e.g., `ml_project`)
- `app_name_upper`: The name of the module in uppercase. (e.g., `ML_PROJECT`)
- `package_name`: The name of the package. (replaces `_` with `-`) (e.g., `ml-project`)
- `env_deferred_logger`: A logger that can be used before the logging system is configured.
    It is later used in `ml_project.utils.log.setup_logging()`

The following functions are exposed:
- `update_data_dirs(data_dir)`: Update the data directories after the package is loaded.

You can configure the app with the following environment variables:
- `{app_name_upper}_CONFIG_DIR`: The directory to search for the `.env` file.
- `{app_name_upper}_DATA_DIR`: The data directory.
- `{app_name_upper}_LOG_LEVEL`: The default log level.
"""

# ruff: noqa: PLW0603
import os
import sys
from os import PathLike
from pathlib import Path

import rich
from dotenv import load_dotenv

from . import _version
from .utils.deferred_logger import DeferredLogger

__version__ = _version.get_versions()["version"]
app_name = __name__
app_name_upper = app_name.upper()
package_name = app_name.replace("_", "-")

# NOTE: The value is None if you haven't installed with `pip install -e .` (development mode).
# We make it None to discourage the use of this path. Only use for development.
PROJECT_DIR: Path | None = Path(__file__).parent.parent.parent
if PROJECT_DIR.name.startswith("python3."):
    PROJECT_DIR = None

env_deferred_logger = DeferredLogger()


def load_dotenv_project_dir_or_config_dir(
    app_name: str = app_name, config_dir_env: str = f"{app_name_upper}_CONFIG_DIR"
) -> Path | None:
    """
    Load .env file from the project directory or ~/.config/$app_name/.
    """
    # if {app_name_upper}_CONFIG_DIR is set, then search .env file in the directory
    config_dir = os.environ.get(config_dir_env, "")
    if config_dir != "":
        dotenv_file = Path(config_dir).resolve() / ".env"
        if not dotenv_file.exists():
            rich.print(f":x: {config_dir_env} is set but {dotenv_file} does not exist.")
            sys.exit(1)
        load_dotenv(dotenv_file, verbose=True)
        env_deferred_logger.info(f"✅ Loaded environment variables from {dotenv_file}")
        return dotenv_file

    # if installed with `pip install -e .`
    # then search .env file is in the project directory
    if PROJECT_DIR is not None:
        dotenv_file = PROJECT_DIR / ".env"
        if dotenv_file.exists():
            load_dotenv(dotenv_file, verbose=True)
            env_deferred_logger.info(
                f"✅ Loaded environment variables from {dotenv_file}"
            )
            return dotenv_file

    # if not found so far, use the default config directory (~/.config/$package_name/)
    from platformdirs import user_config_path

    config_dir = user_config_path(app_name)
    dotenv_file = Path(config_dir) / ".env"
    if dotenv_file.exists():
        load_dotenv(dotenv_file, verbose=True)
        env_deferred_logger.info(f"✅ Loaded environment variables from {dotenv_file}")
        return dotenv_file
    else:
        env_deferred_logger.warning(
            f"⚠️ No .env file found. We recommend you to configure the program with ~/.config/{app_name}/.env.\n"
            "⚠️ You can create a template with `ml-project config`."
        )
        return None


def update_data_dirs(data_dir: str | PathLike):
    """This function is exposed to allow changing the data directories after the package is loaded."""
    global DATA_DIR, LOG_DIR

    DATA_DIR = Path(data_dir)
    LOG_DIR = DATA_DIR / "logs"


dotenv_file = load_dotenv_project_dir_or_config_dir()
if dotenv_file is not None:
    APP_CONFIG_DIR = dotenv_file.parent
else:
    APP_CONFIG_DIR = None


data_dir = os.environ.get(f"{app_name_upper}_DATA_DIR")
if data_dir is None or data_dir == "":
    if PROJECT_DIR is not None:
        data_dir = PROJECT_DIR / "data"
    else:
        from platformdirs import user_data_path

        env_deferred_logger.warning(
            "⚠️ No data directory is set. "
            f"We recommend you to set the data directory with the environment variable {app_name_upper}_DATA_DIR."
        )
        data_dir = user_data_path(__name__)
        env_deferred_logger.warning(f"⚠️ Using {data_dir} as the data directory.")
else:
    data_dir = Path(data_dir)
    if not data_dir.absolute():
        if PROJECT_DIR is not None:
            data_dir = PROJECT_DIR / data_dir
        else:
            data_dir = Path.cwd() / data_dir
        env_deferred_logger.warning(
            "⚠️ It is recommended to set the data directory with an absolute path.\n"
            f"Using {data_dir} as the data directory."
        )


update_data_dirs(data_dir)

default_log_level = os.environ.get(f"{app_name_upper}_LOG_LEVEL")
if default_log_level is None:
    default_log_level = "INFO"
