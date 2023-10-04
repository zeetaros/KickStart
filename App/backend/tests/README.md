# Running Unit Tests
  
In terminal, while in the root directory call `pytest`:  
```sh
pytest 
  
> ========== test session starts ==========
> platform darwin -- Python 3.10.3, pytest-7.1.1, pluggy-1.0.0
> rootdir: /Path/To/App
> plugins: anyio-3.5.0
> collected 1 item

> backend/tests/test_routes/test_users.py .              [100%]
> ========== 1 passed in 0.63s =============
```
which will detect, collect and execute all unit tests.

## Coverage Report
Install `pytest-cov` if not already.
```sh
pip install pytest-cov
```
To generate test coverage report for the `apis` module:
```sh
pytest --cov=apis tests/
```
This will return e.g.
```sh
--------- coverage: platform darwin, python 3.10.12-final-0 ----------
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
apis/__init__.py                           0      0   100%
apis/version1/__init__.py                  0      0   100%
apis/version1/base.py                      7      0   100%
apis/version1/route_general_pages.py       9      1    89%
apis/version1/route_jobs.py               44      3    93%
apis/version1/route_login.py              30     30     0%
apis/version1/route_users.py              11      0   100%
apis/version2/__init__.py                  0      0   100%
apis/version2/route_companies.py          17     17     0%
apis/version2/route_jobs.py               34     34     0%
apis/version2/route_recruiters.py          0      0   100%
----------------------------------------------------------
TOTAL                                    152     85    44%
```
