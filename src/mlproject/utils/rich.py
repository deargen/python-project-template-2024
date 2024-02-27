import os

from ansi2html import Ansi2HTMLConverter
from rich.console import Console
from rich.traceback import Traceback

CONSOLE_WIDTH = 130


def rich_traceback_to_string(tb: Traceback) -> str:
    """
    Convert a rich traceback to a string.

    Examples:
        >>> try:   # doctest: +ELLIPSIS
        ...    1 / 0
        ... except ZeroDivisionError:
        ...     import rich.traceback
        ...     tb = rich.traceback.Traceback()
        ...     print(rich_traceback_to_string(tb))
        ╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
        ...
        ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
        ZeroDivisionError: division by zero
        <BLANKLINE>
    """
    console = Console(
        width=CONSOLE_WIDTH,
        no_color=True,
        highlight=False,
        record=True,
        file=open(os.devnull, "w"),  # noqa: SIM115
    )
    console.print(tb)
    return console.export_text()


def rich_traceback_to_html(tb: Traceback) -> str:
    """
    Convert a rich traceback to an html string.

    Examples:
        >>> try:   # doctest: +ELLIPSIS
        ...    1 / 0
        ... except ZeroDivisionError:
        ...     import rich.traceback
        ...     tb = rich.traceback.Traceback()
        ...     print(rich_traceback_to_html(tb))
        <!DOCTYPE HTML ...
        </html>
        <BLANKLINE>
    """
    console = Console(width=CONSOLE_WIDTH, record=True, file=open(os.devnull, "w"))  # noqa: SIM115
    console.print(tb)

    # NOTE: We don't use `console.export_html()` for the following reasons:
    # 1. It produces a larger file size (2x)
    # 2. It isn't as easy to read as a plain HTML code due to alignment and many html tags.
    # 3. Slack doesn't understand the HTML code produced by `console.export_html()` and treat it as a binary file.

    tb_ansi = console.export_text(styles=True)  # text with ansi color codes
    return Ansi2HTMLConverter().convert(tb_ansi)


def rich_traceback_to_svg(tb: Traceback, title: str) -> str:
    """
    Convert a rich traceback to an svg string.

    Examples:
        >>> try:   # doctest: +ELLIPSIS
        ...    1 / 0
        ... except ZeroDivisionError:
        ...     import rich.traceback
        ...     tb = rich.traceback.Traceback()
        ...     print(rich_traceback_to_svg(tb, "title"))
        <svg class="rich-terminal" ...
        </svg>
        <BLANKLINE>
    """
    console = Console(width=CONSOLE_WIDTH, record=True, file=open(os.devnull, "w"))  # noqa: SIM115
    console.print(tb)

    return console.export_svg(title=title)
