from json import load
from pathlib import Path

import click
from pandas import DataFrame, Series

from src.db_uploader.db import DB
from src.db_uploader.schema import Schema


def formatData(json: dict) -> DataFrame:
    df: DataFrame = DataFrame(data=json)
    df.drop(
        columns=[
            ":@computed_region_awaf_s7ux",
            ":@computed_region_6mkv_f3dw",
            ":@computed_region_vrxf_vc4k",
            ":@computed_region_bdys_3d7i",
            ":@computed_region_43wa_7qmu",
            "location",
        ],
        inplace=True,
    )

    df["line"] = None

    row: Series
    idx: int
    for idx, row in df.iterrows():
        if row["red"]:
            df.loc[idx, "line"] = "red"
        if row["blue"]:
            df.loc[idx, "line"] = "blue"
        if row["g"]:
            df.loc[idx, "line"] = "green"
        if row["brn"]:
            df.loc[idx, "line"] = "brown"
        if row["p"]:
            df.loc[idx, "line"] = "purple"
        if row["pexp"]:
            df.loc[idx, "line"] = "purple-express"
        if row["y"]:
            df.loc[idx, "line"] = "yellow"
        if row["pnk"]:
            df.loc[idx, "line"] = "pink"
        if row["o"]:
            df.loc[idx, "line"] = "orange"

    df.drop(
        columns=[
            "red",
            "blue",
            "g",
            "brn",
            "p",
            "pexp",
            "y",
            "pnk",
            "o",
        ],
        inplace=True,
    )

    return df


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

    df: DataFrame = formatData(json=data)
    print(df)

    db: DB = DB(username=username, password=password, clusterURI=clusterURI)

    if db.ping() is False:
        exit(2)


if __name__ == "__main__":
    main()
