import logging

from motor.motor_asyncio import AsyncIOMotorDatabase

from cfg import get_settings
from mongodb.database import Collections
from mongodb.loaders import BaseLoader
from models import ObjectIdStr

settings = get_settings()


class JobLoader(BaseLoader):
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database=database, collection_name=Collections.job.name)

    async def get_jobs(
        job_ids: list[ObjectIdStr] | None,
    ):
        pass
