import logging
from pathlib import Path
from typing import List, Literal

import click
from pandas import DataFrame

from cta.api.train import TrainAPI
from cta.mongodb import Driver


def ingest(
    api: TrainAPI,
    rt: Literal[
        "red",
        "blue",
        "brn",
        "g",
        "org",
        "p",
        "pink",
        "y",
    ],
) -> DataFrame | None:
    data: DataFrame | None = None

    try:
        data = api.locations(rt=rt)
    except Exception as e:
        logging.error("Status code not 200")
        logging.exception(e)

    return data


def app(
    trainAPI: TrainAPI,
    mdb: Driver,
) -> None:
    data: DataFrame | None = ingest(api=trainAPI)

    if data is not None:
        json: List[dict] = data.to_dict(orient="records")
        mdb.writeDocuments(documents=json)


@click.command()
@click.option(
    "-c",
    "--cluster-uri",
    "mdb_uri",
    type=str,
    required=True,
    help="MongoDB cluster uri",
)
@click.option(
    "-p",
    "--password",
    "mdb_password",
    type=str,
    required=True,
    help="MongoDB account password",
)
@click.option(
    "-u",
    "--username",
    "mdb_username",
    type=str,
    required=True,
    help="MongoDB username",
)
def main(
    mdb_username: str,
    mdb_password: str,
    mdb_uri: str,
) -> None:
    trainAPI: TrainAPI = TrainAPI()
    mdb: Driver = Driver(
        username=mdb_username,
        password=mdb_password,
        uri=mdb_uri,
    )

    mdb.connect()
    mdb.getDatabase()
    mdb.getCollection(name="l_train_locations")

    app(trainAPI=trainAPI, mdb=mdb)


if __name__ == "__main__":
    logFP: Path = Path("l_train_locations.log")

    logging.basicConfig(
        filename=logFP,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    main()
