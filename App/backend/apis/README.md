# APIs Module
   
In general, there are 5 types of operations in any API :

- List 
- Retrieve (get one record from db)
- Post  (create a new record in db)
- Put/Patch  (Update a record)
- Delete    (Delete a record from db)
  
## base.py
This collates all routers information and serves as a single entry point. The idea is to avoid the need to import numerous routes in `main.py`.  

## route_users.py
Function:: `create_user`  
This function will receive user from request and UserCreate scheuma will validate that it has a username, email in proper format, and a password.  
  
The database session will be using the dependency `get_db()` from `session.py`.