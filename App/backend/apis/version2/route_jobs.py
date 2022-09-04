import logging

from fastapi import APIRouter, Request, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi_pagination import Params

from cfg import get_settings
from mongodb.models import Job
from mongodb.loaders import JobLoader
from mongodb.models.base_model import ObjectIdStr
from mongodb.database import DatabaseClient
from utils.exceptions import handle_doc_not_found


router = APIRouter()
settings = get_settings()
motor_engine = DatabaseClient(settings)
job_loader = JobLoader(database=motor_engine.database)

logger = logging.getLogger(__name__)


@router.get(status_code=status.HTTP_200_OK)
@handle_doc_not_found
async def get_jobs(
    request: Request,
    job_ids: list[ObjectIdStr] | None = Query(default=None),
    page_params: Params = Depends(Params),
    loader: JobLoader = Depends(job_loader),
):
    jobs = await loader.get_jobs(job_ids=job_ids)
    paginated_jobs = {
        "items": jobs,
        "page": page_params.page,
        "size": page_params.size,
    }
    return paginated_jobs


@router.get("/company/{company_id}", status_code=status.HTTP_200_OK)
@handle_doc_not_found
async def get_jobs_by_company(
    request: Request, company_id: int, loader: JobLoader = Depends(job_loader)
):
    jobs = await loader.get_jobs(company_id=company_id)
    return jobs


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_job(
    request: Request, job: Job, loader: JobLoader = Depends(job_loader)
):
    response = await loader.create_job(input=job)
    return str(response.inserted_id)


@router.delete("/{job_id}", status_code=status.HTTP_202_ACCEPTED)
@handle_doc_not_found
async def delete_job(
    request: Request, job_id: ObjectIdStr, loader: JobLoader = Depends(job_loader)
):
    return await loader.delete_job(job_id=job_id)
