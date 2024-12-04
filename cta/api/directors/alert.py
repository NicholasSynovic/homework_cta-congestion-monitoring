import typing

import requests
from cta_api.builders.alert import AlertAPIBuilder


class AlertAPIDirector:
    """
    Construct and query Customer Alert API endpoints
    """

    def __init__(self) -> None:
        """
        Instantiate an instance of the Alert API builder
        """
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
        """
        Construct and get the response from the Route Status API.

        Inherits the parameters from cta_api.builders.alert.AlertAPIBuilder.buildRouteStatusAPIURL

        :param timeout: Timeout in seconds for when to close the HTTP connection, defaults to 60
        :type timeout: int, optional
        :return: The HTTP GET response
        :rtype: requests.Response
        """  # noqa: E501
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
        """
        Construct and get the response from the Detailed Alert Status API.

        Inherits the parameters from cta_api.builders.alert.AlertAPIBuilder.buildDetailedAlertsAPIURL

        :param timeout: Timeout in seconds for when to close the HTTP connection, defaults to 60
        :type timeout: int, optional
        :return: The HTTP GET response
        :rtype: requests.Response
        """  # noqa: E501
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
