import typing

import requests
from cta.builders.alert import AlertAPIBuilder


class AlertAPIDirector:
    def __init__(self) -> None:
        self.builder: AlertAPIBuilder = AlertAPIBuilder()

    def getRouteStatus(
        self,
        timeout: int = 60,
        type: typing.Optional[
            typing.List[
                typing.Literal[
                    "bus",
                    "rail",
                    "station",
                    "systemwide",
                ]
            ]
        ] = None,
        routeid: typing.Optional[typing.List[str]] = None,
        stationid: typing.Optional[typing.List[int]] = None,
    ) -> requests.Response:
        url: str = self.builder.buildRouteStatusAPIURL(
            type=type,
            routeid=routeid,
            stationid=stationid,
        )

        resp: requests.Response = requests.get(url=url, timeout=timeout)

        return resp
