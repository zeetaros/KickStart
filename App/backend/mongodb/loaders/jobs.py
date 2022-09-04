import logging

from pydantic import parse_obj_as
from motor.motor_asyncio import AsyncIOMotorDatabase

from cfg import get_settings
from database import Collections
from loaders import BaseLoader
from models import ObjectIdStr, Job
from utils.exceptions import DocumentNotFoundError

settings = get_settings()
logger = logging.getLogger(__name__)


class JobLoader(BaseLoader):
     def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__(database=database, collection_name=Collections.job.name)

     def _build_query(self, job_id: ObjectIdStr | None, job_ids: list[ObjectIdStr] | None, company_id: int | None, location: str | None):
          filters = [{"is_deleted": False }]
          if job_id:
               filters.append({"_id": {"$eq": job_id}})
          if job_ids:
               filters.append({"_id": {"$in": job_ids}})
          if company_id:
               filters.append({"company_id": {"$eq": company_id}})
          if location:
               filters.append({"locations": location})
          return super()._concat_filters(filters=filters)

     async def get_jobs(
          self,
          job_ids: list[ObjectIdStr] | None, 
          company_id: int | None,
          location: str | None,
          projection: dict | None,
    ):
          query = self._build_query(job_ids=job_ids, company_id=company_id, location=location)
          response = await self.paginated_read(query, projection=projection)
          if not response:
               raise DocumentNotFoundError(msg=f"job(s) not found")
          return parse_obj_as(list[Job], response)

     async def create_job(self, input: Job):
          return await self.collection.insert_one({**input.dict()})

     async def delete_job(self, job_id: ObjectIdStr):
          return await self.collection.update_one(
               filter={"_id": {"$eq":job_id}},
               update={"$set": {"is_deleted": True}},
          )
