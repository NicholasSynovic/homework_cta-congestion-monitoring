from json import load
from pathlib import Path
from typing import Any

import click

from src.db_uploader.db import DB


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
    username: str,
    password: str,
    clusterURI: str,
) -> None:
    """
    Steps:

    1. Load JSON file into memory
    2. Connect to the MongoDB database
    3. Ping the connection
    4. Get the correct collection
    5. Load data to MongoDB
    """
    data: dict[str, dict[str, Any]] = load(fp=open(file=inputFile))

    db: DB = DB(username=username, password=password, clusterURI=clusterURI)

    if db.ping() is False:
        print("ERROR: Cannot ping MongoDB")
        exit(1)

    db.getDatabase(databaseName="cta_app")
    db.getCollection(collectionName="arrivals")

    db.writeDocumentsToCollection(documents=data)


if __name__ == "__main__":
    main()
