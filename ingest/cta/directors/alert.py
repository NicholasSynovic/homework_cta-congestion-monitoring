import typing

import requests
from cta.builders.alert import AlertAPIBuilder


class AlertAPIDirector:
    def __init__(self) -> None:
        self.builder: AlertAPIBuilder = AlertAPIBuilder()

    def getRouteStatus(
        self,
        timeout: int = 60,
        type: typing.Optional[typing.List[str | int]] | str = None,
        routeid: typing.Optional[typing.List[str | int]] | str = None,
        stationid: typing.Optional[typing.List[str | int]] | str = None,
    ) -> requests.Response:
        url: str = self.builder.buildRouteStatusAPIURL(
            type=type,
            routeid=routeid,
            stationid=stationid,
        )

        resp: requests.Response = requests.get(url=url, timeout=60)

        return resp


print(AlertAPIDirector().getRouteStatus())
