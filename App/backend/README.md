# Building App with FastAPI

## Start up the App
**Pre-requisite**  
Make sure the database to which the App is connecting is active e.g.  
Spin up the backend postgres database
```sh
brew services start postgresql
```
  
**Steps**  
Start up the application by calling  
```
uvicorn main:app --reload
```
or explicitly specifying port and host
```
uvicorn main:app --reload --port 8000 --host 127.0.0.1
```
Go to the App on browser http://127.0.0.1:8000/  
Or check the API docs http://127.0.0.1:8000/docs This page is useful for getting sample API responses during development.

<br>

## First time set-up of database
Choice of database is postgres.  
  
**Pre-requisite**  
Instruction to get it set up on MacOS.
1) installing postgres with Homebrew
```sh
brew install postgresql
```
2) standing up postgres  
```sh
brew services start postgresql
```
3) creating a new database, user and password
```
postgres=# create database <database name>;
postgres=# create user <username> with encrypted password '<password>';
postgres=# grant all privileges on database <database name> to <username>;
postgres=# exit
```
4) standing down postgres
```sh
brew services stop postgresql
```
Now you can connect to the database on localhost and the default port 5432.

## Reference
Building backend: https://fastapitutorial.com/blogs/  
Standing up database: https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/  &  https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e  