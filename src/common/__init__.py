import ssl
from ssl import SSLContext
from typing import Any, List

from jsonschema import validate
from pandas import DataFrame
from requests import Response, Session, get
from requests.adapters import HTTPAdapter

CTA_L_ABBREVIATIONS: dict[str, str] = {
    "red": "red",
    "blue": "blue",
    "green": "g",
    "brown": "brn",
    "purple": "p",
    "purple-express": "pexp",
    "yellow": "y",
    "pink": "pnk",
    "orange": "o",
}


class SSLAdapter(HTTPAdapter):
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs["ssl_context"] = self.ssl_context
        return super().init_poolmanager(*args, **kwargs)


def getQuery(url: str) -> Response:
    return get(url=url, timeout=60)


def getQueryWithSession(url: str) -> Response:
    context: SSLContext = ssl.create_default_context()
    context.set_ciphers("DEFAULT:@SECLEVEL=1")

    session: Session = Session()
    session.mount("https://", SSLAdapter(ssl_context=context))

    return session.get(url=url, timeout=60)


def extractJSONFromResponse(resp: Response) -> dict | List[dict]:
    if resp.status_code == 200:
        return resp.json()
    else:
        return {}


def dict2df(data: dict) -> DataFrame:
    return DataFrame(data=data)


def validateJSON(data: dict[str, Any], schema: dict[str, Any]) -> bool:
    validate(instance=data, schema=schema)
    return True
