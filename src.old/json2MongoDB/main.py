from json import load
from os import listdir
from pathlib import Path
from typing import List

import click
from db import DB
from progress.bar import Bar


def getJSONFilePaths(dir: Path) -> List[Path]:
    fps: List[Path] = []

    file: str
    for file in listdir(path=dir):
        if file.endswith(".json"):
            fps.append(Path(dir, file))

    return fps


def writeJSON(fps: List[Path], db: DB) -> None:
    with Bar("Writing data to MongoDB 'arrivals' collection...", max=len(fps)) as bar:
        fp: Path
        for fp in fps:
            data: dict = load(fp=open(fp, mode="r"))
            db.writeDocumentsToCollection(documents=data)
            bar.next()


@click.command()
@click.option(
    "-i",
    "--input-dir",
    "inputDir",
    type=click.Path(
        exists=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
        dir_okay=True,
    ),
    nargs=1,
    required=True,
    help="Input directory to read JSON files",
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
    inputDir: Path,
    username: str,
    password: str,
    clusterURI: str,
) -> None:
    jsonFiles: List[Path] = getJSONFilePaths(dir=inputDir)

    db: DB = DB(username=username, password=password, clusterURI=clusterURI)

    if db.ping() is False:
        print("ERROR: Cannot ping MongoDB")
        exit(1)

    db.getDatabase(databaseName="cta_app")
    db.getCollection(collectionName="arrivals")

    writeJSON(fps=jsonFiles, db=db)


if __name__ == "__main__":
    main()
