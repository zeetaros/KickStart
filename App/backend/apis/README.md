# APIs Module
  
## base.py
This collates all routers information and serves as a single entry point. The idea is to avoid the need to import numerous routes in `main.py`.  

## route_users.py
Function:: `create_user`  
This function will receive user from request and UserCreate scheuma will validate that it has a username, email in proper format, and a password.  
  
The database session will be using the dependency `get_db()` from `session.py`.