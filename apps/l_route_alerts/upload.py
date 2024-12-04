import logging
from pprint import pformat
from typing import List

from mdb_handler import MDBDriver


def upload(mdb: MDBDriver, data: List[dict]) -> None:
    mdb.getDatabase()
    mdb.getCollection(name="l_route_alerts")
    mdb.writeDocuments(documents=data)
    logging.info(f"Logged data to MongoDB: {pformat(object=data, indent=4)}")
