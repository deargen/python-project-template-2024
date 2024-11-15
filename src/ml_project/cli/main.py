# Allow print
# Allow many arguments
# Allow relative import from parent
# ruff: noqa: T201 PLR0913 TID252
from pathlib import Path

import rich
import typer
from rich.prompt import Prompt
from rich.syntax import Syntax

app = typer.Typer(
    no_args_is_help=True, context_settings={"help_option_names": ["-h", "--help"]}
)


def version_callback(*, value: bool):
    if value:
        from .. import __version__

        print(__version__)
        raise typer.Exit


@app.callback()
def common(
    ctx: typer.Context,
    *,
    version: bool = typer.Option(
        None, "-v", "--version", callback=version_callback, help="Show version"
    ),
):
    pass


@app.command()
def health():
    from .. import setup_logging
    from ..health import main as health_main

    setup_logging(log_dir=None)
    health_main()


@app.command()
def config(config_dir: Path | None = None):
    """
    Copy the template .env file to the config directory.
    """
    from dotenv import dotenv_values, set_key
    from platformdirs import user_config_path

    from ml_project import APP_NAME, PROJECT_DIR
    from ml_project import __file__ as package_root_file

    template_file = Path(package_root_file).parent / "template.env"
    template_envs = dotenv_values(template_file, interpolate=False)

    template_env_text = template_file.read_text().strip()
    rich.print()
    rich.print(":scroll: Default configuration is as follows:")
    rich.print(
        Syntax(template_env_text, "shell", line_numbers=True, theme="solarized-dark")
    )

    if config_dir is None:
        if PROJECT_DIR is None:
            # if installed properly without -e flag, use the default config directory.
            config_dir = user_config_path(APP_NAME)
        else:
            # if installed as a development package with pip install -e,
            # ask the user to choose which config directory to use.
            user_config_dir = user_config_path(APP_NAME)
            rich.print()
            rich.print("Choose where to store the configuration file:")
            rich.print(f"[bold]1.[/bold] {PROJECT_DIR}/.env -> easy development")
            rich.print(f"[bold]2.[/bold] {user_config_dir}/.env -> production")
            rich.print()
            choice = Prompt.ask("Enter choice", choices=["1", "2"], default="1")
            if choice == "1":
                config_dir = PROJECT_DIR
            else:
                config_dir = user_config_dir

    config_dir = config_dir.resolve()
    config_dir.mkdir(parents=True, exist_ok=True)

    dotenv_file = config_dir / ".env"
    if dotenv_file.exists():
        rich.print()
        rich.print(":scroll: Your current configuration is as follows:")
        rich.print(
            Syntax(
                dotenv_file.read_text().strip(),
                "shell",
                line_numbers=True,
                theme="solarized-dark",
            )
        )

        # Use the existing dotenv file as the base
        # But if there are new variables in the custom file, ignore them.
        current_envs = dotenv_values(dotenv_file, interpolate=False)
        for key in current_envs:
            if key not in template_envs:
                current_envs.pop(key)
        template_envs.update(current_envs)

        # rich.print()
        # confirm = Confirm.ask(
        #     f"File [green]{dotenv_file}[/green] already exists. [red]Overwrite?[/red]",
        #     default=False,
        # )
        # if not confirm:
        #     rich.print("[red]Aborted.[/red]")
        #     sys.exit(1)
    else:
        # First create as the template, because it may have some useful comments and structure.
        dotenv_file.write_text(template_env_text)

    # Then update each variables
    rich.print()
    rich.print("Type in the values for the following variables:")
    for i, (key, value) in enumerate(template_envs.items()):
        choice = Prompt.ask(f"{i+1}/{len(template_envs)}. {key}", default=value)
        if choice is None:
            set_key(dotenv_file, key, "", quote_mode="auto")
        else:
            set_key(dotenv_file, key, choice, quote_mode="auto")

    rich.print()
    rich.print(":scroll: Updated configuration is as follows:")
    rich.print(
        Syntax(
            dotenv_file.read_text().strip(),
            "shell",
            line_numbers=True,
            theme="solarized-dark",
        )
    )
    rich.print()
    rich.print(f"Configuration file created at: '{dotenv_file}'")


def main():
    app()


if __name__ == "__main__":
    main()
