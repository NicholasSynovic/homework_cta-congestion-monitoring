import logging
import time
from pathlib import Path
from pprint import pprint as print
from typing import List

from pandas import DataFrame

from cta_api.alert import AlertAPI


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
    # mdb: mdb_handler.MDBDriver,
) -> None:
    while True:
        data: DataFrame | None = ingest(api=alertAPI)

        if data is None:
            sleep(seconds=sleepSeconds)
            continue

        jsonData: List[dict] = data.to_json()(orient="index")
        print(jsonData)
        quit()


def main(
    mdb_username: str,
    mdb_password: str,
    mdb_uri: str,
    sleepSeconds: int,
) -> None:
    alerts: AlertAPI = AlertAPI()
    # mdb: mdb_handler.MDBDriver = mdb_handler.MDBDriver(
    #     username=mdb_username,
    #     password=mdb_password,
    #     uri=mdb_uri,
    # )

    app(sleepSeconds=sleepSeconds, alertAPI=alerts)


if __name__ == "__main__":
    logFP: Path = Path("l_route_alerts.log")

    logging.basicConfig(
        filename=logFP,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )
