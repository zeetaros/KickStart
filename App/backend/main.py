import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import settings
from apis.base import api_router
from db.session import engine
from db.base import Base

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
loglevels = {
    "CRITICAL": logging.CRITICAL,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "": logging.INFO
}
logger.setLevel(loglevels["DEBUG"])


## Uncomment to get the initial version of the web app
# app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
# @app.get("/")
# def hello_api():
#     return {"msg":"Hello API"}

def include_router(app):
	app.include_router(api_router)

def configure_static(app):
    """ Informing fastapi the location of static files. Whenever it has to search for a static file, e.g. an image, 
        find them inside the static folder only.

    Args:
        app (_type_): FastAPI object
    """
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
    logger.info(f"creating tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()