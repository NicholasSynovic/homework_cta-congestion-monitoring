from json import load
from pathlib import Path

import click

from src.app2.schema import Schema


@click.command()
@click.option(
    "-i",
    "--input",
    "inputFile",
    required=True,
    help="Path to JSON file to load into MongoDB Atlas database",
    type=click.Path(
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "-s",
    "--schema",
    "schemaFile",
    required=True,
    help="Path to JSON Schema file to validate input file",
    type=click.Path(
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
def main(inputFile: Path, schemaFile: Path) -> None:
    data: dict = load(fp=open(file=inputFile))

    schema: Schema = Schema(schemaPath=schemaFile)

    if schema.compare(data=data) is False:
        exit(1)


if __name__ == "__main__":
    main()
