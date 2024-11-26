from pathlib import Path
from typing import List

import click
import cta.stops
from jsonschema import ValidationError
from pandas import DataFrame
from progress.bar import Bar


def getArrivals(
    mapIDs: List[int], arrival: cta.train.Arrivals
) -> dict[str, DataFrame]:  # noqa: E501
    dfs: dict[str, DataFrame] = {}

    with Bar("Querying arrivals API...", max=len(mapIDs)) as bar:
        mapID: int
        for mapID in mapIDs:
            try:
                df: DataFrame = arrival.get(mapid=mapID)
                dfs[mapID] = df
            except ValidationError:
                dfs[mapID] = DataFrame()
            finally:
                bar.next()

    return dfs


def saveJSON(dfs: dict[str, DataFrame], outputDir: Path) -> None:
    keys: List[str] = list(dfs.keys())

    key: str
    for key in keys:
        dfs[key].to_json(
            path_or_buf=Path(outputDir, f"{key}.json"),
            orient="records",
            indent=4,
            index=False,
        )


@click.command()
@click.option(
    "-k",
    "--key",
    "key",
    nargs=1,
    type=str,
    required=True,
    help="CTA API key",
)
@click.option(
    "-o",
    "--output-dir",
    "outputDir",
    nargs=1,
    type=click.Path(
        exists=True,
        dir_okay=True,
        writable=True,
        path_type=Path,
        resolve_path=True,
    ),
    required=True,
    help="Output directory to store JSON files",
)
def main(key: str, outputDir: Path) -> None:
    """
    Export CTA Train REST API endpoint data as JSON files
    """
    arrivalAPI: cta.train.Arrivals = cta.train.Arrivals(key=key)

    stopsDF: DataFrame = cta.stops.Stops().get()
    stops: List[int] = stopsDF["map_id"].apply(str).unique().tolist()

    dfs: dict[str, DataFrame] = getArrivals(
        mapIDs=stops,
        arrival=arrivalAPI,
    )

    saveJSON(dfs=dfs, outputDir=outputDir)


if __name__ == "__main__":
    main()
