import logging
from pathlib import Path
from typing import List

import click
from pandas import DataFrame

from cta.api.system import SystemAPI
from cta.mongodb import Driver


def ingest(api: SystemAPI) -> DataFrame | None:
    data: DataFrame | None = None

    try:
        data = api.getLStopList()
    except Exception as e:
        logging.error("Status code not 200")
        logging.exception(e)

    return data


def app(
    systemAPI: SystemAPI,
    mdb: Driver,
) -> None:
    data: DataFrame | None = ingest(api=systemAPI)

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
    system: SystemAPI = SystemAPI()
    mdb: Driver = Driver(
        username=mdb_username,
        password=mdb_password,
        uri=mdb_uri,
    )

    mdb.connect()
    mdb.getDatabase()
    mdb.getCollection(name="l_stops")

    app(systemAPI=system, mdb=mdb)


if __name__ == "__main__":
    logFP: Path = Path("l_stops.log")

    logging.basicConfig(
        filename=logFP,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    main()
