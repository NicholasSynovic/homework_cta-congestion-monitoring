from json import load
from pathlib import Path

import click
from pandas import DataFrame, Series

from src.db_uploader.db import DB
from src.db_uploader.schema import Schema

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
    "-u",
    "--username",
    "username",
    required=True,
    help="MongoDB Atlas username",
    type=str,
)
@click.option(
    "-p",
    "--password",
    "password",
    required=True,
    help="MongoDB Atlas password",
    type=str,
)
@click.option(
    "-c",
    "--cluster-uri",
    "clusterURI",
    required=True,
    help="MongoDB Atlas clusterURI",
    type=str,
)
def main(
    inputFile: Path,
    schemaFile: Path,
    username: str,
    password: str,
    clusterURI: str,
) -> None:
    data: dict = load(fp=open(file=inputFile))

    schema: Schema = Schema(schemaPath=schemaFile)

    if schema.compare(data=data) is False:
        exit(1)


if __name__ == "__main__":
    main()
