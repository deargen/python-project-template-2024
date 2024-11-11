import inspect
import logging
import os
from collections.abc import Sequence
from datetime import datetime, timezone
from os import PathLike
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

from ml_project import (
    PROJECT_DIR,
    __version__,
    default_log_level,
    env_deferred_logger,
    package_name,
)

logger = logging.getLogger(__name__)

console = Console(
    theme=Theme(
        {
            "logging.level.error": "bold red blink",
            "logging.level.critical": "red blink",
            "logging.level.warning": "yellow",
            "logging.level.success": "green",
        }
    )
)


def setup_logging(
    console_level: int | str = default_log_level,
    log_dir: str | PathLike | None = None,
    output_files: Sequence[str] = (
        "{date:%Y%m%d-%H%M%S}-{name}-{levelname}-{version}.log",
    ),
    file_levels: Sequence[int] = (logging.INFO,),
    *,
    log_init_messages: bool = True,
    console_formatter: logging.Formatter | None = None,
    file_formatter: logging.Formatter | None = None,
):
    r"""
    Setup logging with RichHandler and FileHandler.

    You should call this function at the beginning of your script.

    Args:
        console_level: Logging level for console. Defaults to INFO or env var {app_name_upper}_LOG_LEVEL.
        log_dir: Directory to save log files. If None, only console logging is enabled. Usually set to LOG_DIR.
        output_files: List of output file paths, relative to log_dir. Only applies if log_dir is not None.
        file_levels: List of logging levels for each output file. Only applies if log_dir is not None.
        log_init_messages: Whether to log the initialisation messages.
    """
    assert len(output_files) == len(
        file_levels
    ), "output_files and file_levels must have the same length"

    if log_dir is None:
        output_files = []
        file_levels = []
    else:
        log_dir = Path(log_dir)

    # NOTE: Initialise with NOTSET level and null device, and add stream handler separately.
    # This way, the root logging level is NOTSET (log all), and we can customise each handler's behaviour.
    # If we set the level during the initialisation, it will affect to ALL streams,
    # so the file stream cannot be more verbose (lower level) than the console stream.
    logging.basicConfig(
        format="",
        level=logging.NOTSET,
        stream=open(os.devnull, "w"),  # noqa: SIM115
    )

    # If you want to suppress logs from other modules, set their level to WARNING or higher
    # logging.getLogger('slowfast.utils.checkpoint').setLevel(logging.WARNING)

    console_handler = RichHandler(
        level=console_level,
        show_time=True,
        show_level=True,
        show_path=True,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        console=console,
    )

    if console_formatter is None:
        console_format = logging.Formatter(
            fmt="%(name)s - %(message)s",
            datefmt="%H:%M:%S",
        )
    else:
        console_format = console_formatter
    console_handler.setFormatter(console_format)

    if file_formatter is None:
        f_format = logging.Formatter(
            fmt="%(asctime)s - %(name)s: %(lineno)4d - %(levelname)s - %(message)s",
            datefmt="%y/%m/%d %H:%M:%S",
        )
    else:
        f_format = file_formatter

    function_caller_module = inspect.getmodule(inspect.stack()[1][0])
    if function_caller_module is None:
        name_or_path = "unknown"
    elif function_caller_module.__name__ == "__main__":
        if function_caller_module.__file__ is None:
            name_or_path = function_caller_module.__name__
        elif PROJECT_DIR is not None:
            # Called from files in the project directory.
            # Instead of using the __name__ == "__main__", infer the module name from the file path.
            name_or_path = function_caller_module.__file__.replace(
                str(PROJECT_DIR) + "/", ""
            ).replace("/", ".")
            # Remove .py extension
            name_or_path = Path(name_or_path).with_suffix("")
        else:
            # Called from somewhere outside the project directory.
            # Use the script name, like "script.py"
            name_or_path = Path(function_caller_module.__file__).name
    else:
        name_or_path = function_caller_module.__name__

    log_path_map = {
        "name": name_or_path,
        "version": __version__,
        "date": datetime.now(timezone.utc),
    }

    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)

    if log_init_messages:
        logger.info(f"{package_name} {__version__}")
        env_deferred_logger.flush(logger)

    if log_dir is not None:
        log_paths = []
        for output_file, file_level in zip(output_files, file_levels, strict=True):
            log_path_map["levelname"] = logging._levelToName[file_level]
            log_path = log_dir / output_file.format_map(log_path_map)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            f_handler = logging.FileHandler(log_path)
            f_handler.setLevel(file_level)
            f_handler.setFormatter(f_format)

            # Add handlers to the logger
            root_logger.addHandler(f_handler)

        if log_init_messages:
            for log_path in log_paths:
                logger.info(f"Logging to {log_path}")


def main():
    logger.info("Hello, world!")
    raise Exception("Test exception")  # noqa: TRY002


if __name__ == "__main__":
    try:
        setup_logging(log_dir=None)
        main()
    except Exception:
        logger.exception("Exception occurred")
