from pathlib import Path

import click


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
def main(inputFile: Path) -> None:
    pass


if __name__ == "__main__":
    main()
