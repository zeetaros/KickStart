import logging
import typing as tp

from fastapi import APIRouter, HTTPException, Depends, status, Response, Request

from cfg import get_settings
from mongodb.models import Company
from mongodb.loaders import CompanyLoader
from mongodb.database import DatabaseClient
from utils.exceptions import handle_doc_not_found

router = APIRouter()
settings = get_settings()
logger = logging.getLogger(__name__)


db_client = DatabaseClient(settings)


@router.get("/{company_id}", response_model=Company)
@handle_doc_not_found
async def get_company(company_id):
    loader = CompanyLoader(database=db_client.database)
    return await loader.get_company(company_id=company_id)
