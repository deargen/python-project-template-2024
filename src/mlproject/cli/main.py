import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def version():
    from .. import __version__

    print(__version__)  # noqa: T201


@app.command()
def health():
    from ..health.__main__ import main as health_main
    from ..utils.log import setup_logging

    setup_logging(output_files=[], file_levels=[])
    health_main()


def main():
    app()


if __name__ == "__main__":
    main()
