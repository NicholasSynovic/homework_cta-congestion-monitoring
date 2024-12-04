import logging
from pathlib import Path
from time import sleep, time

import click
from pandas import DataFrame

from cta_api.alert import AlertAPI


def app(sleepSeconds: int, api: AlertAPI, outputDirectory: Path) -> None:
    """
    Working code to access and download data from CTA L Routes API

    Downloads data to a timestamp JSON file

    :param sleepSeconds: Number of seconds to sleep until a call is made again
    :type sleepSeconds: int
    :param api: AlertAPI class
    :type api: AlertAPI
    :param outputDirectory: Directory to save JSON files
    :type outputDirectory: Path
    """
    while True:
        fp: Path = Path(outputDirectory, f"{int(time())}_alerts_routes.json")
        logging.info(f"File to save data to assigned: {fp}")

        logging.info("Sending get query to Route Status API")

        try:
            df: DataFrame = api.route_status(type=["rail"])
        except ValueError as ve:
            logging.error("Status code not 200")
            logging.exception(msg=ve)
        else:
            df.to_json(path_or_buf=fp, indent=4, orient="records")
            logging.info(msg=f"Wrote JSON to {fp}")

        logging.info(f"Sleeping for {sleepSeconds} seconds")
        sleep(sleepSeconds)


@click.command()
@click.option(
    "-o",
    "--output",
    "outputDirectory",
    required=True,
    help="Directory to store alerts in JSON format",
    type=click.Path(
        exists=False,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "-l",
    "--logs",
    "logDirectory",
    required=True,
    help="Directory to store logs",
    type=click.Path(
        exists=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "-s",
    "--sleep",
    "sleepSeconds",
    required=True,
    help="Number of seconds to sleep before retrieving new queries",
    type=int,
    required=False,
    default=300,
    show_default=True,
)
def main(outputDirectory: Path, logDirectory: Path, sleepSeconds: int) -> None:
    """
    CTA Routes Alerts Ingest Utility

    Download the latest alerts per CTA L Route (e.g., Red, Blue, Yellow) to a JSON file
    """  # noqa: E501
    logFP: Path = Path(logDirectory, "ingest_CTARoutesAlerts.log")

    logging.basicConfig(
        filename=logFP,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    logging.info(msg="Started application")

    api: AlertAPI = AlertAPI()

    app(sleepSeconds=sleepSeconds, api=api, outputDirectory=outputDirectory)


if __name__ == "__main__":
    main()
