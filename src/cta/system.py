import pandas
import requests


class SystemAPI:
    """
    Top level interface to working with the CTA System API
    """

    def __init__(self) -> None:
        pass

    def getLStopList(self) -> pandas.DataFrame:
        """
        Get data from the L Stop List API endpoint.

        :raises ValueError: Raised if the response status code != 200
        :return: A pandas.DataFrame of the response
        :rtype: pandas.DataFrame
        """
        resp: requests.Response = requests.get(
            url="https://data.cityofchicago.org/resource/8pix-ypme.json",
            timeout=60,
        )

        if resp.status_code != 200:
            raise ValueError("System API endpoint status code != 200")

        df: pandas.DataFrame = pandas.DataFrame(data=resp.json())
        df["latitude"] = df["location"].str.get("latitude")
        df["longitude"] = df["location"].str.get("longitude")
        df.drop(columns=["location"], inplace=True)

        return df
