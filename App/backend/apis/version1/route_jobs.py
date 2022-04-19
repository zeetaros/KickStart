from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retrieve_job, list_jobs, update_job_by_id, delete_job_by_id

router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_job(job:JobCreate, db:Session=Depends(get_db)):
     current_user = 1
     job = create_new_job(job=job, db=db, owner_id=current_user)
     return job

@router.get("/get/{id}", response_model=ShowJob)
def read_job(id:int, db:Session=Depends(get_db)):
     job = retrieve_job(id=id, db=db)
     if not job:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Job with this id {id} does not exist"
                         )
     return job

@router.get("/get_exact_owner/{owner_id}", response_model=ShowJob)
def read_job_one(owner_id:int, db:Session=Depends(get_db)):
     try:
          job = retrieve_job(id=owner_id, db=db, validate_uniqueness=True)
     except Exception:
          raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                              detail=f"Job with this owner id {owner_id} is not unique or does not exist"
                         )
     return job

@router.get("/all", response_model=List[ShowJob])
def read_jobs(db:Session=Depends(get_db)):
     jobs = list_jobs(db=db)
     return jobs

@router.put("/update/{id}")
def update_job(id:int, job:JobCreate, db:Session=Depends(get_db)):
     current_user_id = 1
     message = update_job_by_id(id=id, job=job, db=db, owner_id=current_user_id)
     if not message:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Job with id {id} not found"
                         )
     return {"msg": "Successfully updated data!"}

@router.delete("/delete/{id}")
def delete_job(id:int, db:Session=Depends(get_db)):
     current_user_id = 1
     message = delete_job_by_id(id=id, db=db, owner_id=current_user_id)
     if not message:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detial=f"Job with id {id} not found"
                         )
     return {"msg": "Successfully deleted data!"}
     