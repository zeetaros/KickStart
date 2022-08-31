import dataclasses
import typing as tp
from enum import Enum
from dataclasses import dataclass

import asyncio
import pymongo
from pymongo import ASCENDING, DESCENDING
from motor.motor_asyncio import AsyncIOMotorClient


@dataclasses.dataclass
class CollectionSpec:
    name: str
    indices: tp.Optional[tp.List] = dataclasses.field(default_factory=list)
    index_kwargs: tp.Optional[tp.Dict[str, tp.Any]] = dataclasses.field(
        default_factory=list
    )


class Collections(Enum):
    job = CollectionSpec(
        name="jobs",
        indices=[("expiration_date", DESCENDING), ("_id", ASCENDING)],
        index_kwargs={"index_name": "job_id", "unique": True},
    )
    company = CollectionSpec(
        name="companies", indices=[("country", ASCENDING), ("company_name", ASCENDING)]
    )
    recruiter = CollectionSpec(
        name="recruiters",
        indices=[("first_name", ASCENDING)],
        index_kwargs={"index_name": "recruiter"},
    )


class DatabaseClient:
    def __init__(self, _settings):
        self.client = AsyncIOMotorClient(
            host=_settings.MONGO_HOST,
            username=_settings.MONGO_USER,
            password=_settings.MONGO_PASS,
        )
        self.client.get_io_loop = asyncio.get_running_loop
        self.database = self.client.get_database(
            _settings.MONGO_DB, read_preference=pymongo.ReadPreference.SECONDARY
        )
