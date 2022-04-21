import json
import pytest
from fastapi import status

@pytest.fixture(scope="class")
def prep_data_in_db(client_cls):
     data_1 = {
          "id": 1,
          "title": "SDE super",
          "company": "doogle",
          "company_url": "www.doogle.com",
          "location": "UK, London",
          "description": "python",
          "date_posted": "2022-03-20",
          "owner_id": 1
     }
     data_2 = {
          "title": "SDE super",
          "company": "goggle",
          "company_url": "www.goggle.com",
          "location": "US, New York",
          "description": "java",
          "date_posted": "2022-04-18",
          "owner_id": 1
     }
     response = client_cls.post("jobs/create-job/", json.dumps(data_1))
     response = client_cls.post("jobs/create-job/", json.dumps(data_2))

def test_create_job(client):
     data = {
          "title": "SDE super",
          "company": "doogle",
          "company_url": "www.doogle.com",
          "location": "UK, London",
          "description": "python",
          "date_posted": "2022-03-20"
     }
     response = client.post("/jobs/create-job/", json.dumps(data))
     assert response.status_code == 200
     assert response.json()["company"] == "doogle"
     assert response.json()["description"] == "python"


@pytest.mark.usefixtures("prep_data_in_db")
class TestReadJob():
     def test_read_job(self, client_cls):
          response = client_cls.get("/jobs/get/1")
          assert response.status_code == 200
          assert response.json()["title"] == "SDE super"
     
     def test_read_unique_job_error(self, client_cls):
          response = client_cls.get("/jobs/get_exact_owner/1")
          assert response.status_code == 500
     
     def test_read_empty_job_error(self, client_cls):
          response = client_cls.get("/jobs/get_exact_owner/3")
          assert response.status_code == 500

     def test_read_all_jobs(self, client_cls):
          response = client_cls.get("/jobs/all")
          assert response.status_code == 200
          assert response.json()[0]
          assert response.json()[1]


def test_update_job(client):
     data = {
          "title": "SDE super",
          "company": "doogle",
          "company_url": "www.doogle.com",
          "location": "UK, London",
          "description": "python",
          "date_posted": "2022-03-20"
     }
     client.post("/jobs/create-job/", json.dumps(data))
     data["title"] = "test new title"
     response = client.put("/jobs/update/1", json.dumps(data))
     assert response.json()["msg"] == "Successfully updated data!"
     response_read = client.get("/jobs/get/1")
     assert response_read.json()["title"] == "test new title"

def test_delete_job(client):
     data = {
          "title": "SDE super",
          "company": "doogle",
          "company_url": "www.doogle.com",
          "location": "UK, London",
          "description": "python",
          "date_posted": "2022-03-20"
     }
     client.post("/jobs/create-job/", json.dumps(data))
     response = client.delete("/jobs/delete/1")
     response_read = client.get("/jobs/get/1")
     assert response_read.status_code == status.HTTP_404_NOT_FOUND