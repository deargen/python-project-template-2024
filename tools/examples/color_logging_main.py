"""Example main function template."""
# 다른 import 하기 전, 맨 위에 추가하면 import 과정에서 생기는 에러들을 rich로 출력할 수 있습니다.
import rich.traceback

rich.traceback.install(show_locals=True)

import logging

from mlproject.utils import setup_logging

logger = logging.getLogger(__name__)


def main():
    """
    Log an info message and an exception.

    Raises:
        Exception:
    """
    logger.info("This is an info message")
    raise Exception("This is an exception")


if __name__ == "__main__":
    try:
        setup_logging()
        main()
    except Exception:
        logger.exception("Exception occurred")
