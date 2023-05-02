# Database(db) Module
## Repository/
  
The "repository" design pattern was adopted to allow the separation of database interaction (e.g. database orm logic) from FastAPI routes. This enable easy configurations and changes in future should we wish to switch database or ORM.  