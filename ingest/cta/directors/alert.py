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

    def getDetailedAlerts(
        self,
        timeout: int = 60,
        activeonly: bool = None,
        accessibility: bool = None,
        planned: bool = None,
        bystartdate: int = None,
        recentdays: int = None,
        routeid: typing.Optional[typing.List[str]] = None,
        stationid: typing.Optional[typing.List[int]] = None,
    ) -> str:
        url: str = self.builder.buildDetailedAlertsAPIURL(
            activeonly=activeonly,
            accessibility=accessibility,
            planned=planned,
            bystartdate=bystartdate,
            recentdays=recentdays,
            routeid=routeid,
            stationid=stationid,
        )

        resp: requests.Response = requests.get(url=url, timeout=timeout)

        return resp
