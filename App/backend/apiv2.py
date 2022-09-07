from fastapi import FastAPI
from fastapi_pagination import add_pagination

from apis.version2 import route_companies, route_jobs, route_recruiters

COMPANY_ROUTER = "company"
JOB_ROUTER = "job"
RECRUITER_ROUTER = "recruiter"


def add_routers(api_kwargs):
    api = FastAPI(**api_kwargs)

    routers = {
        COMPANY_ROUTER: route_companies,
        JOB_ROUTER: route_jobs,
        RECRUITER_ROUTER: route_recruiters,
    }

    for name, router in routers.items():
        add_pagination(router.router)
        api.include_router(
            router.router,
            prefix=f"/{name}",
            tags=[name],
            responses={404: {"description": "Not Found"}},
        )
    return api
