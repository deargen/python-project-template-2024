import logging
from io import BytesIO, IOBase

import cairosvg
from matplotlib.figure import Figure
from PIL import Image
from slack_sdk.web import WebClient

from . import channel_id as default_channel_id
from . import client as default_client

logger = logging.getLogger(__name__)
warned = False


def warn_once():
    global warned
    if not warned:
        logger.warning(
            "You tried to send messages on Slack, but the token is not set. All messages will be ignored."
        )
        warned = True


def send_text(
    text: str,
    *,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    return client.chat_postMessage(channel=channel_id, text=text)


def send_text_as_file(
    *,
    filename: str,
    content: str,
    title: str,
    initial_comment: str | None = None,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    return client.files_upload_v2(
        filename=filename,
        content=content,
        title=title,
        channel=channel_id,
        initial_comment=initial_comment,
    )


def send_divider(
    *,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    return client.chat_postMessage(
        channel=channel_id,
        text="Divider",
        blocks=[
            {"type": "divider"},
        ],
    )


def send_file(
    *,
    filename: str,
    file: str | bytes | IOBase,
    title: str,
    snippet_type: str | None = None,
    initial_comment: str | None = None,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    return client.files_upload_v2(
        filename=filename,
        file=file,
        title=title,
        channel=channel_id,
        snippet_type=snippet_type,
        initial_comment=initial_comment,
    )


def send_matplotlib_fig(
    filename: str,
    fig: Figure,
    title: str,
    initial_comment: str | None = None,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    buf = BytesIO()
    fig.savefig(buf, format="pdf")
    buf.seek(0)
    return send_file(
        filename=filename,
        file=buf,
        title=title,
        initial_comment=initial_comment,
        channel_id=channel_id,
        client=client,
    )


def send_pil_image(
    filename: str,
    image: Image.Image,
    title: str,
    initial_comment: str | None = None,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    buf = BytesIO()
    image.save(buf, format="png")
    buf.seek(0)
    return send_file(
        filename=filename,
        file=buf,
        title=title,
        initial_comment=initial_comment,
        channel_id=channel_id,
        client=client,
    )


def send_svg_as_pdf(
    filename: str,
    svg_file: str | bytes | IOBase,
    title: str,
    initial_comment: str | None = None,
    channel_id: str | None = None,
    client: WebClient | None = None,
):
    """
    Send an SVG file as a PDF file.

    Slack does not support previewing SVG files, so we convert it to PDF.
    """
    if client is None:
        client = default_client
    if client is None:
        warn_once()
        return None
    if channel_id is None:
        channel_id = default_channel_id
        assert channel_id is not None

    pdf_buf = BytesIO()

    if isinstance(svg_file, str | bytes):
        cairosvg.svg2pdf(bytestring=svg_file, write_to=pdf_buf)
    elif isinstance(svg_file, IOBase):
        cairosvg.svg2pdf(file_obj=buf, write_to=pdf_buf)
    else:
        raise ValueError(f"Unsupported type {type(svg_file)}")

    pdf_buf.seek(0)

    return client.files_upload_v2(
        filename=filename,
        file=pdf_buf,
        title=title,
        channel=channel_id,
        initial_comment=initial_comment,
    )
