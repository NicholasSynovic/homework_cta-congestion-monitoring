from pathlib import Path

import click
import ibis
from polars import DataFrame
from requests import Response

from src.common import dict2df, extractJSONFromResponse, getQuery
from src.l_stop_handler import API


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
    4. Drop :@ keys
    5. Convert to DF
    6. Load into DB
    """

    resp: Response = getQuery(url=API)
    data: list[dict] = extractJSONFromResponse(resp=resp)

    # from pprint import pprint as print
    print([f'"{key}":{value}' for key, value in data[0].items()])
    quit()

    df: DataFrame = dict2df(data=data)

    df["longitude"] = df["location"].map_elements(lambda x: x["longitude"])
    df["latitude"] = df["location"].map_elements(lambda x: x["latitude"])

    print(df.columns)
    quit()

    con = ibis.connect(resource=f"sqlite:///{outputFile}")
    con.create_table(name="stops", obj=df)

    print(con.list_tables())


if __name__ == "__main__":
    main()
