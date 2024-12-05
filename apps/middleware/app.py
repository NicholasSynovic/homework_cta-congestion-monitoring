import os
from collections import defaultdict
from time import time
from typing import List

from fastapi import FastAPI
from pymongo.cursor import Cursor

from cta.mongodb import Driver


class Cache:
    def __init__(self) -> None:
        self.previousTime: int = 0

        self.l_route_alerts: List[dict] = []
        self.l_station_alerts: List[dict] = []
        self.l_stops: List[dict] = []

    def checkTime(self) -> bool:
        """
        If the current time is over 5.5 minutes greater than the previous time, return True. Else, return False

        :return: True if enough time has passed to update the cache, else False
        :rtype: bool
        """  # noqa: E501

        currentTime: int = int(time())
        timeDiff: int = currentTime - self.previousTime

        if timeDiff >= 330:
            self.previousTime = currentTime
            return True
        else:
            return False


cache: Cache = Cache()

mdb: Driver = Driver(
    username=os.environ["mdb_username"],
    password=os.environ["mdb_password"],
    uri=os.environ["mdb_uri"],
)

mdb.connect()
mdb.getDatabase()


app: FastAPI = FastAPI()


@app.get(path="/")
def helloWorld() -> dict[str, str]:
    return {"msg": "Hello World"}


@app.get(path="/getRouteAlerts")
def getRouteAlerts() -> List[dict]:
    if cache.checkTime():
        cache.l_route_alerts = []

        cursor: Cursor = mdb.getLatest_LRouteAlerts()

        doc: dict
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            cache.l_route_alerts.append(doc)

    return cache.l_route_alerts


@app.get(path="/getStationAlerts")
def getStationAlerts() -> List[dict]:
    if cache.checkTime():
        cache.l_station_alerts = []

        cursor: Cursor = mdb.getLatest_LStationAlerts()

        doc: dict
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            cache.l_station_alerts.append(doc)

    return cache.l_station_alerts


@app.get(path="/getStations")
def getStations() -> List[dict]:
    uniqueMapIDs: dict[str, bool] = defaultdict(bool)

    if cache.checkTime():
        cache.l_station_alerts = []

        cursor: Cursor = mdb.get_LStops()

        doc: dict
        for doc in cursor:
            if uniqueMapIDs[doc["map_id"]]:
                continue
            else:
                uniqueMapIDs[doc["map_id"]] = True

            doc["_id"] = str(doc["_id"])
            cache.l_stops.append(doc)

    return cache.l_stops


@app.get(path="/getRoutes")
def getRoutes() -> dict[str, str]:
    return {
        "red": "Red",
        "blue": "Blue",
        "g": "Green",
        "brn": "Brown",
        "p": "Purple",
        "pexp": "Purple Express",
        "y": "Yellow",
        "pnk": "Pink",
        "o": "Orange",
    }


@app.get(path="/getSpecificStation")
def getSpecificStation(stationID: str) -> List[dict]:
    uniqueStations: dict[str, bool] = defaultdict(bool)
    stations: List[dict] = []

    getStations()

    station: dict
    for station in cache.l_stops:
        name: str = station["station_name"]
        if uniqueStations[name]:
            continue
        else:
            uniqueStations[name] = True

        if station[stationID]:
            stations.append(station)

    return stations
