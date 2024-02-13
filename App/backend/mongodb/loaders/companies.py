import logging

from motor.motor_asyncio import AsyncIOMotorDatabase

from cfg import get_settings
from mongodb.database import Collections
from mongodb.loaders import BaseLoader


class CompanyLoader(BaseLoader):
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database=database, collection_name=Collections.company.name)

    async def get_companies(company_ids: list[int]):
        pass
