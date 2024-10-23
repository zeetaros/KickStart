import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from cfg import get_settings
from apiv2 import add_routers
from mongodb.database import start_application, end_application

settings = get_settings()
logger = logging.getLogger(__name__)
logger.debug("Initialise logger from main module")

description = """
A place that broadcast new job opportunities. 🚀

## General users

You can **read jobs**.

## Recruiters

You will be able to:

* **Create jobs
* **Read job
"""

common_kwargs = {
    "openapi_url": "/api/v1/openapi.json",
    "docs_url": "/docs",
}

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="2.0",
    on_startup=[start_application],
    on_shutdown=[end_application],
    description=description,
)

# Cross-Origin Resource Sharing, detail https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Enforces that all incoming requests must either be https or wss.
app.add_middleware(HTTPSRedirectMiddleware)

apis = add_routers(api_kwargs=common_kwargs)


app.mount("/api/v2", apis)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
