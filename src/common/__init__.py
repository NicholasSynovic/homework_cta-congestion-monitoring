from polars import DataFrame
from requests import Response, get


def getQuery(url: str) -> Response:
    return get(url=url, timeout=60)


def extractJSONFromResponse(resp: Response) -> dict:
    if resp.status_code == 200:
        return resp.json()
    else:
        return {}


def dict2df(data: dict) -> DataFrame:
    return DataFrame(data=data)
