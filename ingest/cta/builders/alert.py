import functools
import typing

import cta.builders

SAFE_JOIN: functools.partial = functools.partial(cta.builders._safeJoin)
VALID_TYPE: typing.List[str] = ["bus", "rail", "station", "systemwide"]


class AlertAPIBuilder:
    """
    Chicago Transit Authority (CTA) Customer Alerts API endpoint builder

    https://www.transitchicago.com/developers/alerts/
    """  # noqa: E501

    def __init__(
        self,
        outputType: typing.Literal["xml", "json"] = "json",
    ) -> None:
        """
        :param outputType: Specifies the format of the response content, defaults to "json"
        :type outputType: typing.Literal[`xml`, `json`], optional
        :raises ValueError: If outputType is not `xml` or `json`, a ValueError is raised
        """  # noqa: E501
        if (outputType != "xml") and (outputType != "json"):
            raise ValueError("outputType must be either `xml` or `json`")

        self.outputType = outputType

        self.constructor: functools.partial = functools.partial(
            cta.builders._constructAPI,
            outputType=self.outputType,
        )

    def buildRouteStatusAPIURL(
        self,
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
        routeid: typing.Optional[typing.List[str]] | str = None,
        stationid: typing.Optional[typing.List[int]] | str = None,
    ) -> str:
        if (type) and not isinstance(type, list):
            raise TypeError("`type` must be a list")

        _type: str
        for _type in type:
            try:
                VALID_TYPE.index(_type)
            except ValueError:
                raise ValueError(
                    f"`{_type}` is not a valid input to parameter `type`"
                )  # noqa: E501

        url: str = "http://www.transitchicago.com/api/1.0/routes.aspx"

        return self.constructor(
            url=url,
            type=SAFE_JOIN(data=type),
            routeid=SAFE_JOIN(data=routeid),
            stationid=SAFE_JOIN(data=stationid),
        )

    def buildDetailedAlertsAPIURL(
        self,
        activeonly: bool = None,
        accessibility: bool = None,
        planned: bool = None,
        routeid: typing.Optional[typing.List[str | int]] | str = None,
        stationid: typing.Optional[typing.List[str | int]] | str = None,
        bystartdate: str = None,
        recentdays: int = None,
    ) -> str:
        """
        buildDetailedAlertsAPIURL _summary_

        _extended_summary_

        :param activeonly: _description_, defaults to None
        :type activeonly: bool, optional
        :param accessibility: _description_, defaults to None
        :type accessibility: bool, optional
        :param planned: _description_, defaults to None
        :type planned: bool, optional
        :param routeid: _description_, defaults to None
        :type routeid: typing.Optional[typing.List[str  |  int]] | str, optional
        :param stationid: _description_, defaults to None
        :type stationid: typing.Optional[typing.List[str  |  int]] | str, optional
        :param bystartdate: _description_, defaults to None
        :type bystartdate: str, optional
        :param recentdays: _description_, defaults to None
        :type recentdays: int, optional
        :return: _description_
        :rtype: str
        """  # noqa: E501
        url: str = "http://www.transitchicago.com/api/1.0/routes.aspx"

        return self.constructor(
            url=url,
            activeonly=activeonly,
            accessibility=accessibility,
            planned=planned,
            routeid=SAFE_JOIN(data=routeid),
            stationid=SAFE_JOIN(data=stationid),
            bystartdate=bystartdate,
            recentdays=recentdays,
        )
