import logging
import time
from pathlib import Path
from typing import List

import click
from pandas import DataFrame

from cta.api.alert import AlertAPI
from cta.mongodb import Driver


def ingest(api: AlertAPI) -> DataFrame | None:
    data: DataFrame | None = None

    try:
        data = api.route_status(type=["rail"])
    except Exception as e:
        logging.error("Status code not 200")
        logging.exception(e)

    return data


def sleep(seconds: int) -> None:
    logging.info(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


def app(
    sleepSeconds: int,
    alertAPI: AlertAPI,
    mdb: Driver,
) -> None:
    while True:
        data: DataFrame | None = ingest(api=alertAPI)

        if data is not None:
            json: List[dict] = data.to_dict(orient="records")
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
def main(
    mdb_username: str,
    mdb_password: str,
    mdb_uri: str,
    sleepSeconds: int = 300,
) -> None:
    alerts: AlertAPI = AlertAPI()
    mdb: Driver = Driver(
        username=mdb_username,
        password=mdb_password,
        uri=mdb_uri,
    )

    mdb.connect()
    mdb.getDatabase()
    mdb.getCollection(name="l_route_alerts")

    app(sleepSeconds=sleepSeconds, alertAPI=alerts, mdb=mdb)


if __name__ == "__main__":
    logFP: Path = Path("l_route_alerts.log")

    logging.basicConfig(
        filename=logFP,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    main()
