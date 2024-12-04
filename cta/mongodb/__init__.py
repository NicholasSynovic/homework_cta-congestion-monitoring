import logging
from typing import List, Literal
from urllib.parse import quote_plus

from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Driver:
    def __init__(self, username: str, password: str, uri: str) -> None:
        self.client: MongoClient | None = None
        self.database: Database | None = None
        self.collection: Collection | None = None

        self.username: str = quote_plus(string=username)
        self.password: str = quote_plus(string=password)
        self.uri: str = uri

        self.connectURI: str = (
            f"mongodb+srv://{self.username}:{self.password}@{self.uri}"
        )

    def connect(self) -> bool:
        CONNECT: bool = True

        self.client = MongoClient(
            host=self.connectURI,
            server_api=ServerApi(version="1"),
        )

        try:
            self.client.admin.command("ping")
        except Exception as e:
            CONNECT = False
            logging.error(msg=e)

        return CONNECT

    def getDatabase(self) -> None:
        self.database = self.client.get_database(name="cta")

    def getCollection(self, name: str) -> None | Literal[False]:
        try:
            self.collection = self.database.get_collection(name=name)
        except Exception as e:
            logging.error(msg=e)
            return False

    def writeDocuments(self, documents: List[dict]) -> None:
        self.collection.insert_many(documents=documents)
