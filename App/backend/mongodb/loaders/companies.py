import logging
import typing as tp

from motor.motor_asyncio import AsyncIOMotorDatabase

from cfg import get_settings
from mongodb.database import Collections


class CompanyLoader:
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database=database, collection_name=Collections.company.name)

    async def get_company(company_id: int):
        pass
