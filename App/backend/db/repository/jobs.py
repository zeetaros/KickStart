from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate,db: Session,owner_id:int):
     job_object = Job(**job.dict(),owner_id=owner_id)
     db.add(job_object)
     db.commit()
     db.refresh(job_object)
     return job_object

def retrieve_job(id:int, db:Session, validate_uniqueness:bool=False):
     if validate_uniqueness:
          try:
          # Get one, and exactly one result. In all other cases it will raise an exception 
               item = db.query(Job).filter(Job.owner_id == id).one()
          except MultipleResultsFound as e:
               #TODO: add handling
               raise e
          except NoResultFound as e:
               #TODO: add handling
               raise e
          except Exception as e:
               raise e
     else:
          # Get the first result of possibly many, without raising exceptions
          item = db.query(Job).filter(Job.id == id).first()
          return item

def list_jobs(db:Session):
     jobs = db.query(Job).all().filter(Job.is_active == True)
     return jobs