from typing import Any, List

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pandas import DataFrame
from requests import Response, get

from src.common.schemas import Schema


def getQuery(url: str) -> Response:
    return get(url=url, timeout=60)


def extractJSONFromResponse(resp: Response) -> dict | List[dict]:
    if resp.status_code == 200:
        return resp.json()
    else:
        return {}


def dict2df(data: dict) -> DataFrame:
    return DataFrame(data=data)


def validateJSON(data: dict[str, Any], schema: Schema) -> bool:
    try:
        validate(instance=data, schema=schema)
    except ValidationError as exception:
        print(exception)
        return False
    else:
        return True
