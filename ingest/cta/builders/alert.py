import functools
import typing

import cta.builders


class AlertAPIBuilder:
    """
     _summary_

    _extended_summary_
    """

    def __init__(
        self,
        outputType: typing.Literal["xml", "json"] = "json",
    ) -> None:
        """
        __init__ _summary_

        _extended_summary_

        :param outputType: _description_, defaults to "json"
        :type outputType: typing.Literal[&quot;xml&quot;, &quot;json&quot;], optional
        :raises ValueError: _description_
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
        type: typing.Optional[typing.List[str | int]] | str = None,
        routeid: typing.Optional[typing.List[str | int]] | str = None,
        stationid: typing.Optional[typing.List[str | int]] | str = None,
    ) -> str:
        """
        buildRouteStatusAPIURL _summary_

        _extended_summary_

        :param type: _description_, defaults to None
        :type type: typing.Optional[typing.List[str  |  int]] | str, optional
        :param routeid: _description_, defaults to None
        :type routeid: typing.Optional[typing.List[str  |  int]] | str, optional
        :param stationid: _description_, defaults to None
        :type stationid: typing.Optional[typing.List[str  |  int]] | str, optional
        :return: _description_
        :rtype: str
        """  # noqa: E501
        url: str = "http://www.transitchicago.com/api/1.0/routes.aspx"

        return self.constructor(
            url=url,
            type=",".join(type),
            routeid=",".join(routeid),
            stationid=",".join(stationid),
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
            routeid=",".join(routeid),
            stationid=",".join(stationid),
            bystartdate=bystartdate,
            recentdays=recentdays,
        )
