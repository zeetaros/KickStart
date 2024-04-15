# Airflow
## Initial configuration
```sh
export AIRFLOW_HOME=~/airflow
```

The system environment variable `AIRFLOW_HOME` should link to the directory where `airflow.cfg` is stored. Then, Airflow will apply the configurations set in
`airflow.cfg`.
- `dags_folder`: directory where DAGs are stored. DAGs stored in this directory will be visible on web GUI. If DAGs is loaded properly, they will appear when check with Airflow CLI
    ```sh
    airflow dags list
    ```

## Set up backend database
### SQLite
SQLite comes with Anaconda installation of Python. It is useful for creating in-memory database and for testing.

```sh
# Windows
export SQL_ALCHEMY_CONN=sqlite:////C: \Users\<username>/airflow/airflow.db

# Linux
export SQL_ALCHEMY_CONN=sqlite:////home/<username>/airflow/airflow.db

# initialise a SQLite database named "airflow.db"
airflow db init
```

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

<br>

## User Management
If running Airflow for the first time, create a user:
```sh
airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password <your_password>
```

<br>

## Front End GUI
Simplest way to do quick start:
```sh
airflow standalone
```
This initialises the database, creates a user, starts scheduler and all other components. Then Visit `localhost:8080` in browser to access the web
GUI.  

The standard way to stand up Airflow web server:
```sh
airflow webserver

# Or specify port & hostname
airflow webserver --port 8080 --hostname 0.0.0.0
```
During development, to access a remote webserver from a local browser, first stand up the webserver on remote on `http://0.0.0.0`, with chosen port e.g. *8080*. Find the remote server IP address
```sh
hostname -I
```
In local, connect to the remote server's IP address on a browser via:
```
http://<remote ip address>:8080
```
*P.S. starting up the webserver only provide a front end GUI. To run DAGs on the GUI, a scheduler is required.  

<br>

## Scheduler
To start up Airflow scheduler:
```sh
airflow scheduler
```
DAGs triggered can now be picked up by the workers for execution.

### Multiple Schedulers
When running with SQLite and SequentialExecutor, only 1 thread is allowed. Hence, it might  encounter subag triggered stuck in "queued" / "running" status because there is no more resources can be used to execute them. This can be resolved by stand up a second scheduler by:
```sh
airflow scheduler --skip-serve-logs
```
However, the proper way to handle this problem is to use a proper backend database e.g. Postgres or MySQL together with a CeleryExecutor or KubernetesExecutor.

<br>

## Task dependencies
To form the DAG's structure, we need to define dependencies between each task. One way is to use the `>>` symbol as shown below:
```py
task1 >> task2 >> task3
```
Note that one task may have multiple dependencies:
```py
task1 >> [task2, task3]
```
The other way is through the `set_downstream`, `set_upstream` functions:
```py
t1.set_downstream([t2, t3])
```

### Task triggers
Operators have a trigger_rule that defines how the task gets triggered. The default all _success rule dictates that the task should be triggered when all upstream dependent tasks have reached the success state. If you don"t specify the upstream, then the task will be triggered when you trigger the dag.  

Once you created a task and mentioned the dag, it will be part of that dag. Setting up/down stream is only for establishing a relationship between tasks, which task will be triggered will be determined by upstream task and trigger rule.  

*Reference: https://stackoverflow. com/questions/60088432/tasks-show-up-even-when-i-am-not-giving-a-upstream-or-downstream-in-airfLow*


<br>

## Tips
### Configuration
In the Airflow configuration file (`airflow.cfg`):
1. Disable Example DAGs to prevent the automatic loading of example DAGs during initialisation.
    ```
    load_examples = False
    ```
2. Configure the DAGs Directory to specify the location where your DAG files will reside. This allows you to organise DAGs in a specific directory.
    ```
    dags_folder = ~/airflow/dags
    ```

### Development
#### List DAGS
To list DAGs recognised by Airflow:
```sh
airflow dags list
```

#### Validate DAGs
To validate dags before start up webserver:
```sh
airflow dags list-import-errors
```
This would attempt to validate DAGs before loading to check if DAGs are written properly.  
Alternatively, test if DAG raise error while loading through a loader test:
```sh
python <dag_file.py>
```

#### Test loading time
Use the Linux built-in `time` command to check if the DAG loads faster after an optimisation:
```sh
# For example
time python airflow/example_dags/dag_file.py
```

#### Troubleshoot
__jinja2.exceptions.TemplateNotFound__ when running shell scripts  
Solution: add a space after the script name in cases where you are directly calling a bash scripts in the `bash_command` attribute of `BashOperator`
- this is because the Airflow tries to apply a Jinja template to it, which will fail.
```py
t2 = Bashoperator(
    task_id='sleep', 
    bash_command="/home/user/test.sh", # This fails with "Jinja template not found error
    bash_command="/home/user/test.sh ", # This works (has a space after)
)
```
*Reference: https://cwiki.apache.org/confLuence/pages/viewpage.action?pageId=62694614*
