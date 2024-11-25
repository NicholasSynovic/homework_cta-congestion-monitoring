from typing import Any, List
from urllib.parse import quote_plus

from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class DB:
    def __init__(self, username: str, password: str, clusterURI: str) -> None:
        self.database: Database | None = None
        self.collection: Collection | None = None

        self.username: str = quote_plus(string=username)
        self.password: str = quote_plus(string=password)

        self.uri: str = (
            f"mongodb+srv://{self.username}:{self.password}@{clusterURI}"  # noqa: E501
        )

        self.client: MongoClient = MongoClient(
            host=self.uri,
            server_api=ServerApi("1"),
        )

    def ping(self) -> bool:
        try:
            self.client.admin.command(command="ping")
        except Exception:
            return False
        else:
            return True

    def close(self) -> None:
        self.client.close()

    def getDatabase(self, databaseName: str) -> None:
        self.database = self.client.get_database(name=databaseName)

    def getCollection(
        self,
        collectionName: str,
    ) -> None:
        self.collection = self.database.get_collection(name=collectionName)

    def writeDocumentsToCollection(
        self,
        documents: List[dict[str, Any]],
    ) -> None:
        self.collection.insert_many(documents=documents)
