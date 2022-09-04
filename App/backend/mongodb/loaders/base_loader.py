import logging
import typing as tp

import pymongo.database
import pymongo.errors
from motor.motor_asyncio import (
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
    AsyncIOMotorCursor,
)
from database import Collections

logger = logging.getLogger(__name__)


class BaseLoader:
    def __init__(self, database: AsyncIOMotorDatabase, collection_name: str):
        self.database = database
        self.collection = database[collection_name]

    async def _concat_filters(self, filters: list[dict[str, tp.Any]]):
        query = {}
        if len(filters) > 1:
            query = {"$and": filters}
        elif len(filters) == 1:
            query = filters[0]

        logger.debug(f"{self.__class__.__name__} constructed query: {query}")
        return query

    async def read(
        self, query: dict | None, projection: dict | None, **kwargs: dict | None
    ) -> list[dict]:
        cursor = self.collection.find(filter=query, projection=projection, **kwargs)
        return await self.to_list(cursor=cursor)

    async def paginated_read(
        self,
        page_number: int | None,
        page_size: int | None,
        query: dict | None,
        projection: dict | None,
        **kwargs: dict | None,
    ):
        if not page_number and not page_size:
            return await self.read(query=query, projection=projection, **kwargs)
        skip = ((page_number - 1) * page_size) if page_number > 0 else 0
        cursor = (
            self.collection.find(filter=query, projection=projection, **kwargs)
            .skip(skip)
            .limit(page_size)
        )
        return await self.to_list(cursor=cursor)

    @staticmethod
    async def to_list(cursor: AsyncIOMotorCursor):
        return [doc async for doc in cursor]

    async def create_index(
        self,
        index_name: str,
        index_fields: list[tuple[str, int]],
        unique: bool = False,
    ):
        existing_indexes = await self.collection.index_information()
        if index_name in existing_indexes:
            if sorted(index_fields) != sorted(existing_indexes[index_name].get("key")):
                self.collection.drop_index(index_name)
            else:
                raise pymongo.errors.OperationFailure("Index already exists")
        response = await self.collection.create_index(
            keys=index_fields, name=index_name, unique=unique
        )
        return response

    async def count_documents(self, filters: dict):
        return await self.collection.count_documents(filter=filters or {})
