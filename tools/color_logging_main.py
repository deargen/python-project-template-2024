# 맨 위에 install() 코드 넣어주시면 어떤 모듈에서 에러가 나든 깔끔한 traceback이 나와 디버깅이 좋습니다
from rich.traceback import install

install()

import logging
import os

import mlproject
from rich.logging import RichHandler

# 옵션으로 `from accelerate.logging import get_logger`
# 사용하시면 로깅할 때 main_process_only=False, in_order=True 등 옵션 사용 가능합니다
# https://huggingface.co/docs/accelerate/package_reference/logging
logger = logging.getLogger(__name__)

log_path = "train.log"


def main():
    # Write main code here
    pass


if __name__ == "__main__":
    """
    Initialise with NOTSET level and null device, and add stream handler separately.
    This way, the root logging level is NOTSET (log all), and we can customise each handler's behaviour.
    If we set the level during the initialisation, it will affect to ALL streams,
    so the file stream cannot be more verbose (lower level) than the console stream.
    """
    logging.basicConfig(
        format="",
        level=logging.NOTSET,
        stream=open(os.devnull, "w"),
    )

    # If you want to suppress logs from other modules, set their level to WARNING or higher
    # logging.getLogger('slowfast.utils.checkpoint').setLevel(logging.WARNING)

    console_handler = RichHandler(
        level=logging.INFO,
        show_time=True,
        show_level=True,
        show_path=True,
        rich_tracebacks=True,
    )
    console_format = logging.Formatter(
        fmt="%(name)s - %(message)s",
        datefmt="%m/%d %H:%M:%S",
    )
    console_handler.setFormatter(console_format)

    f_handler = logging.FileHandler(log_path)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter(
        fmt="%(asctime)s - %(name)s: %(lineno)4d - %(levelname)s - %(message)s",
        datefmt="%y/%m/%d %H:%M:%S",
    )
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(f_handler)

    try:
        logger.info(f"mlproject {mlproject.__version__}")
        main()
        logger.info("💖 Successfully completed!")
    except Exception:
        logger.exception("Exception occurred")
