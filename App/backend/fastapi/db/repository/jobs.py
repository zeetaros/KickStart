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
     jobs = db.query(Job).filter(Job.is_active == True).all()
     return jobs

def update_job_by_id(id:int, job:JobCreate, db:Session, owner_id):
     existing_job = db.query(Job).filter(Job.id == id)
     if not existing_job.first():
          return 0
     # Update dictionary with new key value of owner id
     job.__dict__.update(owner_id=owner_id)
     existing_job.update(job.__dict__)
     db.commit()
     return 1

def delete_job_by_id(id:int, db:Session, owner_id):
     existing_job = db.query(Job).filter(Job.id == id)
     if not existing_job.first():
          return 0
     existing_job.delete(synchronize_session=False)
     db.commit()
     return 1