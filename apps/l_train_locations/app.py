import logging
import time
from pathlib import Path
from typing import List

import click
from pandas import DataFrame

from cta.api.train import TrainAPI
from cta.mongodb import Driver


def ingest(api: TrainAPI) -> List[DataFrame] | None:
    data: List[DataFrame] = []
    rt: List[str] = ["red", "blue", "brn", "g", "org", "p", "pink", "y"]

    route: str
    for route in rt:
        df: DataFrame | None = None

        try:
            df = api.locations(rt=route)
        except Exception as e:
            logging.error("Status code not 200")
            logging.exception(e)
        else:
            data.append(df)

    return data


def sleep(seconds: int) -> None:
    logging.info(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


def app(
    sleepSeconds: int,
    trainAPI: TrainAPI,
    mdb: Driver,
) -> None:
    data: List[DataFrame] | None = ingest(api=trainAPI)

    df: DataFrame
    for df in data:
        if df is not None:
            json: List[dict] = df.to_dict(orient="records")
            mdb.writeDocuments(documents=json)

    sleep(seconds=sleepSeconds)


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
@click.option(
    "-k",
    "--key",
    "cta_key",
    type=str,
    required=True,
    help="CTA developer key",
)
def main(
    mdb_username: str,
    mdb_password: str,
    mdb_uri: str,
    cta_key: str,
    sleepSeconds: int = 300,
) -> None:
    trainAPI: TrainAPI = TrainAPI(key=cta_key)
    mdb: Driver = Driver(
        username=mdb_username,
        password=mdb_password,
        uri=mdb_uri,
    )

    mdb.connect()
    mdb.getDatabase()
    mdb.getCollection(name="l_train_locations")

    app(sleepSeconds=sleepSeconds, trainAPI=trainAPI, mdb=mdb)


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
