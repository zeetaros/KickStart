import time
import logging
import psycopg2
import contextlib


@contextlib.contextmanager
def db_connection(host, user, passwd, dbname, port):
    counter = 0
    authentication = False

    while counter < 3 and authentication == False:
        try:
            connection = psycopg2.connect(
                host=host, user=user, password=passwd, database=dbname, port=port
            )
            authentication = True
        except:
            logging.error(
                f"Failed to connect to the database. {counter} attempt(s) made."
            )
            counter += 1
            time.sleep(10)

    connection.autocommit = True
    try:
        yield connection
    except Exception:
        logging.error("Closing database connection! Rollback.")
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()


@contextlib.contextmanager
def cursor(host, username, password, dbname, port):
    with db_connection(
        host=host, user=username, passwd=password, dbname=dbname, port=port
    ) as conn:
        cursor = conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
