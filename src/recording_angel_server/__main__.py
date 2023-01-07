"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Recording Angel Server."""


if __name__ == "__main__":
    main(prog_name="recording-angel-server")  # pragma: no cover
