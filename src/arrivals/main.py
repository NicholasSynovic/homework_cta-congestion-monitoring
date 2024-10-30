from pathlib import Path
from typing import Any, List, Tuple

import click
import ibis
from ibis import BaseBackend, Table
from pandas import DataFrame
from requests import Response

from src.common import (
    CTA_L_ABBREVIATIONS,
    extractJSONFromResponse,
    getQueryWithSession,
    validateJSON,
)
from src.common.schemas import TrainArrivals


def getMapIDs(con: BaseBackend, line: str) -> List[str]:
    table: Table = con.tables["stops"]
    query: Table = (
        table.filter(table[line] == True).select("map_id").distinct()  # noqa: #712
    )
    return sorted(query.to_pandas()["map_id"].tolist())


def produceSlices(data: List[str]) -> List[Tuple[str, str, str]]:
    foo: List[Tuple[str, str, str]] = []

    for i in range(0, len(data), 4):
        foo.append(tuple(data[i : i + 3]))  # noqa: E203

    return foo


def constructAPIURLs(data: List[Tuple[str, str, str]], key: str) -> List[str]:
    urls: List[str] = []

    apiTemplate: str = f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&outputType=JSON"

    datum: Tuple[str, str, str]
    for datum in data:
        url: str = apiTemplate

        for idx in range(len(datum)):
            url = url + f"&mapid={datum[idx]}"

        urls.append(url)

    return urls


def queryAPI(urls: List[str]) -> List[dict[str, Any]]:
    data: List[dict[str, Any]] = []

    url: str
    for url in urls:
        resp: Response = getQueryWithSession(url=url)
        json: dict = extractJSONFromResponse(resp=resp)

        if validateJSON(data=json, schema=TrainArrivals().schema) is False:
            continue

        data.extend(json["ctatt"]["eta"])

    return data


@click.command()
@click.option(
    "-k",
    "--key",
    "key",
    required=True,
    nargs=1,
    type=str,
    help="CTA API key",
)
@click.option(
    "-l",
    "--line",
    "line",
    required=True,
    nargs=1,
    type=click.Choice(
        choices=[
            "red",
            "blue",
            "green",
            "brown",
            "purple",
            "purple-exp",
            "yellow",
            "pink",
            "orange",
        ]
    ),
    help="CTA L train line API endpoint to access",
)
@click.option(
    "-i",
    "--input",
    "inputDB",
    required=True,
    nargs=1,
    type=click.Path(
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    help="Path to CTA L train station SQLite3 database",
)
@click.option(
    "-o",
    "--output",
    "outputFile",
    required=True,
    nargs=1,
    type=click.Path(
        exists=False,
        file_okay=True,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
    help="Path to store CTA L train arrivals in JSON file",
)
def main(key: str, line: str, inputDB: Path, outputFile: Path) -> None:
    lStopAbbreviation: str = CTA_L_ABBREVIATIONS[line]

    con: BaseBackend = ibis.connect(resource=f"sqlite:///{inputDB}")
    mapIDs: List[str] = getMapIDs(con=con, line=lStopAbbreviation)

    mapIDSlices: List[Tuple[str, str, str, str]] = produceSlices(data=mapIDs)

    apiURLs: List[str] = constructAPIURLs(data=mapIDSlices, key=key)

    data: List[dict[str, Any]] = queryAPI(urls=apiURLs)

    DataFrame(data=data).to_json(path_or_buf=outputFile, indent=4, index=False,orient="records",)


if __name__ == "__main__":
    main()
