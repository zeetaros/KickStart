CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
-- PostgreSQL 15 requires additional privileges:
USE airflow_db;
GRANT ALL ON SCHEMA public TO airflow_user;