from pathlib import Path

import click
from cta.alert import AlertAPI
from pandas import DataFrame


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
def main(outputFP: Path) -> None:
    api: AlertAPI = AlertAPI()
    df: DataFrame = api.route_status(type=["station"])

    df.to_json(path_or_buf=outputFP, indent=4, orient="records")


if __name__ == "__main__":
    main()
