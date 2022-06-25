## Quick Start
To spin up Celery, follow the below steps while you are under the root directory of your Celery project (i.e. `~/celery-scheduler/`)



1. Run Redis:
```bash
./redis-stable/src/redis-server
```

** 1st time set up
Download from http://download.redis.io/redis-stable.tar.gz
Run below to unzip and install
```bash
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```
Recommend adding below to `.bash_profile`
```sh
export PATH=$PATH:$HOME/<path>/<to>/redis-stable/src
```

2. Run celerybeat:
```bash
celery -A app.celery beat --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid
```

3. Run celery worker:
```bash
celery -A app.celery worker --loglevel=INFO
```

<br>

## Workers
You can start multiple workers on the same machine, but be sure to name each individual worker by specifying a node name with the `--hostname` argument:  
```bash
celery -A app.celery worker --loglevel=INFO --concurrency=10 -n worker1@%h
$ celery -A app.celery worker --loglevel=INFO --concurrency=10 -n worker2@%h
$ celery -A app.celery worker --loglevel=INFO --concurrency=10 -n worker3@%h
```

*In the example above, each worker would run 10 processes in parallel. That is, 3 x 10 processes in total.*

<br>

## Supervisors
Supervisor works by executing programmes through configuration files that it is fed with. These configuration files inform Supervisor which executables to run, the environment variables that come with it, how the output will be handled.  
All programs run under Supervisor must be run in a non-daemonising mode (a.k.a. 'foreground mode', executables which takes control of the terminal and requires you to press Ctrl-C to regain control of your terminal). e.g. Redis, Celerybeat and Celery workers.

<br>

## More about Celery
### Primitives
__group__

- The group primitive is a signature that takes a list of tasks that should be applied in parallel.

__chain__

- The chain primitive lets us link together signatures so that one is called after the other, essentially forming a chain of callbacks.

__chord__

- A chord is just like a group but with a callback. A chord consists of a header group and a body, where the body is a task that should execute after all of the tasks in the header are complete.

Reference: https://docs.celeryproject.org/en/stable/userguide/canvas.html

<br>

### Concurrency

<br>

### Retry Policy
Reference: https://docs.celeryproject.org/en/stable/userguide/calling.html
