# Airflow

## Setup

### PostgreSQL
Using Postgres (PG) as backend. 

[Only First-time] install and initialise a database:
```sh
brew install postgresql@14

export PGDATA=~/PostgreSQL/data

initdb
```

**Manual Start/Stop PG server**
```sh
pg_ctl -D /Users/<username>/PostgreSQL/data -l logfile start

pg_ctl stop
```

**Automatically Start PG server**
```sh
brew services start postgresql
```
This will start up PG as computer starts, it can be terminated by
```sh
brew services stop postgresql
```
The corresponding stop command should be issued for each choice of start-up command but not mixed.

**Check Running Processes**
```sh
ps aux | grep postgres
ps -e | grep postgres
```

**Start Using `psql`**
By running `initdb` (to create the first database) command it doesn't have your username as any database name. It has a database named *postgres*. If you don't have another database named your username, you need to do:
```sh
psql -d postgres
```
While in psql instance, it will show the host "postgres=#". A simple database can be created:
```
postgres=# CREATE DATABASE airflow_db;
postgres=# CREATE USER airflow_user WITH PASSWORD '12345678';
postgres=# GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
postgres=# GRANT ALL ON SCHEMA public TO airflow_user;
```

## SQLAlchemy
If you created a new Postgres account for Airflow:
- The default search_path for new Postgres user is: "$user", public, no change is needed.
If you use a current Postgres user with custom search_path, search_path can be changed by the command:
```sql
ALTER USER airflow_user SET search_path = public;
```

For instance, you can specify a database schema where Airflow will create its required tables. If you want Airflow to install its tables in the airflow schema of a PostgreSQL database, specify these environment variables:
```sh
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql://postgres@localhost:5432/my_database?options=-csearch_path%3Dairflow"
export AIRFLOW__DATABASE__SQL_ALCHEMY_SCHEMA="airflow"
```

