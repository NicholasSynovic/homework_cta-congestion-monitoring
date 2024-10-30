from pathlib import Path

import click


@click.command()
@click.option(
    "-o",
    "--output",
    "outputFile",
    type=click.Path(
        exists=False, file_okay=True, writable=True, resolve_path=True, path_type=Path
    ),
    required=True,
    help="Path to write SQLite3 database to",
)
def main() -> None:
    pass
