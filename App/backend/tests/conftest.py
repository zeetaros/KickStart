import os
import sys
import pytest
import logging
from typing import Any
from typing import Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Include backend directory in sys.path to enable import from db, main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.base import Base
from db.session import SQLALCHEMY_DATABASE_URL, get_db
from apis.version1.base import api_router

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def start_application():
     app = FastAPI()
     app.include_router(api_router)
     return app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(
     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Use connect_args parameter only with sqlite
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# =============== Fixtures for Function ===============

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
     """
     This is a fixture function, which will run before each test function to which it is applied.
     Fixtures are used to feed some data to the tests such as database connections, URLs to test and some input data.

     This particular fixture is for creating a fresh database on each test case.
     """
     logger.info(f"Running fixture: app")
     Base.metadata.create_all(engine) # Create the tables
     _app = start_application()
     yield _app
     Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
     logger.info(f"Running fixture: db_session")
     connection = engine.connect()
     transaction = connection.begin()
     session = SessionTesting(bind=connection)
     yield session # Use the session in tests
     session.close()
     transaction.rollback() # Each test should be independent, hence, resetting the changes in the db tables (or even creating a new db for each test).
     connection.close()

@pytest.fixture(scope="function")
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
     """
     Create a new FastAPI TestClient that uses the `db_session` fixture to override the 
     `get_db` dependency that is injected into routes.
     """
     logger.info(f"Running fixture: client")
     def _get_test_db():
          try:
               yield db_session
          finally:
               pass

     app.dependency_overrides[get_db] = _get_test_db
     with TestClient(app) as client:
          logger.info("Cold start completed for: client")
          yield client


# =============== Fixtures for Class ===============

@pytest.fixture(scope="class")
def app_cls() -> Generator[FastAPI, Any, None]:
     """
     This is a fixture function, which will run before each test function to which it is applied.
     Fixtures are used to feed some data to the tests such as database connections, URLs to test and some input data.

     This particular fixture is for creating a fresh database on each test case.
     """
     logger.info(f"Running fixture: app")
     Base.metadata.create_all(engine) # Create the tables
     _app = start_application()
     yield _app
     Base.metadata.drop_all(engine)

@pytest.fixture(scope="class")
def db_session_cls(app_cls: FastAPI) -> Generator[SessionTesting, Any, None]:
     logger.info(f"Running fixture: db_session")
     connection = engine.connect()
     transaction = connection.begin()
     session = SessionTesting(bind=connection)
     yield session # Use the session in tests
     session.close()
     transaction.rollback() # Each test should be independent, hence, resetting the changes in the db tables (or even creating a new db for each test).
     connection.close()

@pytest.fixture(scope="class")
def client_cls(app_cls: FastAPI, db_session_cls: SessionTesting) -> Generator[TestClient, Any, None]:
     """
     Create a new FastAPI TestClient that uses the `db_session` fixture to override the 
     `get_db` dependency that is injected into routes.
     """
     logger.info(f"Running fixture: client")
     def _get_test_db():
          try:
               yield db_session_cls
          finally:
               pass

     app_cls.dependency_overrides[get_db] = _get_test_db
     with TestClient(app_cls) as client:
          logger.info("Cold start completed for: client_cls")
          yield client
