import logging
from pathlib import Path
from time import time

import click
from pandas import DataFrame

from cta_api.alert import AlertAPI


@click.command()
@click.option(
    "-o",
    "--output",
    "outputFP",
    required=True,
    help="Path to store alerts",
    type=click.Path(
        exists=False,
        file_okay=True,
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
def main(outputFP: Path, logDirectory: Path) -> None:
    logFP: Path = Path(logDirectory, f"cta-alerts.{time()}.log")

    logging.basicConfig(
        filename=logFP,
        filemode="w",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    logging.info(msg="Started application")

    api: AlertAPI = AlertAPI()

    logging.info("Sending get query to Route Status API")

    try:
        df: DataFrame = api.route_status(type=["rail", "station"])
    except ValueError as ve:
        logging.error("Status code not 200")
        logging.exception(msg=ve)
    else:
        df.to_json(path_or_buf=outputFP, indent=4, orient="records")
        logging.info(msg=f"Wrote JSON to {outputFP}")


if __name__ == "__main__":
    main()
