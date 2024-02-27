"""Example main function template."""
import rich.traceback
from dotenv import load_dotenv

# 다른 import 하기 전, 맨 위에 추가하면 import 과정에서 생기는 에러들을 rich로 출력할 수 있습니다.
rich.traceback.install(show_locals=True)
load_dotenv()

import logging
import socket
import traceback

from mlproject.utils import setup_logging
from mlproject.utils.rich import (
    rich_traceback_to_html,
    rich_traceback_to_string,
    rich_traceback_to_svg,
)
from mlproject.utils.slack.send_only import (
    send_svg_as_pdf,
    send_text_as_file,
)

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
        slack_text = f"Exception occurred from host {socket.gethostname()}\n\n```{traceback.format_exc()}```"

        tb = rich.traceback.Traceback(show_locals=True)
        tb_text = rich_traceback_to_string(tb)
        # NOTE: slack is stupid and having special characters in the file makes it think it's a binary file.
        # We wrap the text with triple quotes so slack thinks it's a python code and it shows the preview.
        tb_text = '""""""\n' + tb_text
        tb_html = rich_traceback_to_html(tb)
        tb_svg = rich_traceback_to_svg(
            tb, title=f"Exception occurred from host {socket.gethostname()}"
        )

        send_text_as_file(
            filename="traceback.txt",
            content=tb_text,
            title="traceback.txt",
            initial_comment=slack_text,
        )
        send_text_as_file(
            filename="traceback.html",
            content=tb_html,
            title="traceback.html",
            initial_comment="* To view the HTML without downloading:\n\n"
            "1. Open in new window (it will open in Chrome)\n2. Copy all content\n"
            "3. <F12> to open Dev Tools\n4. Elements -> <html> right click -> Edit as HTML\n"
            "5. Paste\n6. <Enter> to apply changes",
        )
        send_svg_as_pdf(
            filename="traceback.pdf",
            svg_file=tb_svg,
            title="traceback.pdf",
        )
