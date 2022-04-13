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