import typing

import cta.builders


class TrainAPIBuilder:
    """
     _summary_

    _extended_summary_
    """

    def __init__(self, key: str) -> None:
        self.key = key

    def buildArrivalsAPIURL(
        self,
        mapid: typing.Optional[int] = None,
        stpid: typing.Optional[int] = None,
        max: typing.Optional[int] = None,
        rt: typing.Optional[str] = None,
    ) -> str:
        """
        buildArrivalsAPIURL _summary_

        _extended_summary_

        :param mapid: _description_, defaults to None
        :type mapid: typing.Optional[int], optional
        :param stpid: _description_, defaults to None
        :type stpid: typing.Optional[int], optional
        :param max: _description_, defaults to None
        :type max: typing.Optional[int], optional
        :param rt: _description_, defaults to None
        :type rt: typing.Optional[str], optional
        :raises ValueError: _description_
        :return: _description_
        :rtype: str
        """
        if (mapid is None) and (stpid is None):
            raise ValueError("Either mapid or stpid must be set")

        url: str = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?outputType=JSON"  # noqa: E501

        return cta.builders._constructAPI(
            url=url,
            key=self.key,
            mapid=mapid,
            stpid=stpid,
            max=max,
            rt=rt,
        )

    def buildFollowThisTrainAPIURL(self, runnumber: int) -> str:
        """
        buildFollowThisTrainAPIURL _summary_

        _extended_summary_

        :param runnumber: _description_
        :type runnumber: int
        :return: _description_
        :rtype: str
        """
        url: str = "http://lapi.transitchicago.com/api/1.0/ttfollow.aspx?outputType=JSON"  # noqa: E501

        return cta.builders._constructAPI(
            url=url,
            key=self.key,
            runnumber=runnumber,
        )

    def buildLocationsAPIURL(self, key: str, rt: str) -> str:
        """
        buildLocationsAPIURL _summary_

        _extended_summary_

        :param rt: _description_
        :type rt: int
        :return: _description_
        :rtype: str
        """
        url: str = "http://lapi.transitchicago.com/api/1.0/ttfollow.aspx?outputType=JSON"  # noqa: E501

        return cta.builders._constructAPI(url=url, key=self.key, rt=rt)
