from pathlib import Path
from typing import Any, List

import click
import ibis
from pandas import DataFrame
from requests import Response

from src.common import dict2df, extractJSONFromResponse, getQuery, validateJSON
from src.common.schemas import LStops
from src.stops import API


def extractLongitudeLatitude(data: List[dict[str, Any]]) -> List[dict[str, Any]]:
    foo: List[dict[str, Any]] = []

    bar: dict[str, Any]
    for bar in data:
        locationKV: dict[str, Any] = bar.pop("location")
        bar["longitude"] = locationKV["longitude"]
        bar["latitude"] = locationKV["latitude"]
        foo.append(bar)

    return foo


@click.command()
@click.option(
    "-o",
    "--output",
    "outputFile",
    type=click.Path(
        exists=False, file_okay=True, writable=True, resolve_path=True, path_type=Path
    ),
    required=True,
    help="Path to write SQLite3 database to",
)
def main(outputFile: Path) -> None:
    """
    Steps:

    1. Get JSON response
    2. Validate JSON response
    3. Extract longitude and latitude from location key
    5. Convert to DF
    4. Drop :@ keys
    6. Load into DB
    """

    resp: Response = getQuery(url=API)
    data: List[dict[str, Any]] = extractJSONFromResponse(resp=resp)

    if validateJSON(data=data, schema=LStops().schema) is False:
        print(
            "ERROR: Something has changed with the Chicago Data Portal API schema",
        )
        exit(0)

    data = extractLongitudeLatitude(data=data)

    df: DataFrame = dict2df(data=data)
    df = df.loc[:, ~df.columns.str.startswith(":@")]

    con = ibis.connect(resource=f"sqlite:///{outputFile}")
    con.create_table(name="stops", obj=df, overwrite=True)

    exit(0)


if __name__ == "__main__":
    main()
