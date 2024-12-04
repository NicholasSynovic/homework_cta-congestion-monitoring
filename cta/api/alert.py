from time import time

import pandas
import requests

import cta.api
import cta.api.directors
import cta.api.directors.alert


class AlertAPI:
    """
    Top level interface to working with the CTA Customer Alerts API
    """

    def __init__(self) -> None:
        self.director: cta.api.directors.alert.AlertAPIDirector = (
            cta.api.directors.alert.AlertAPIDirector()
        )

    def route_status(self, **kwargs) -> pandas.DataFrame:
        """
        Get data from the Route Status API endpoint.

        Inherits parameters from `cta.api.directors.alert.getRouteStatus()`

        :raises ValueError: Raised if the response status code != 200
        :return: A pandas.DataFrame of the response
        :rtype: pandas.DataFrame
        """
        resp: requests.Response = self.director.getRouteStatus(**kwargs)

        if resp.status_code != 200:
            raise ValueError("Route Status API endpoint status code != 200")

        ctaRoutes: dict = resp.json()["CTARoutes"]["RouteInfo"]

        df: pandas.DataFrame = pandas.DataFrame(data=ctaRoutes)
        df["RouteURL"] = df["RouteURL"].str.get("#cdata-section")
        df["Time"] = int(time())
        df.reset_index(drop=True, inplace=True)

        return df

    def detailed_status(self, **kwargs) -> pandas.DataFrame:
        """
        Get data from the Detailed Status API endpoint.

        Inherits parameters from `cta.api.directors.alert.getDetailedAlerts()`

        :raises ValueError: Raised if the response status code != 200
        :return: A pandas.DataFrame of the response
        :rtype: pandas.DataFrame
        """
        resp: requests.Response = self.director.getDetailedAlerts(**kwargs)

        if resp.status_code != 200:
            raise ValueError("Detailed Status API endpoint status code != 200")

        ctaRoutes: dict = resp.json()["CTARoutes"]["RouteInfo"]

        df: pandas.DataFrame = pandas.DataFrame(data=ctaRoutes)
        df.reset_index(drop=True, inplace=True)

        return df
