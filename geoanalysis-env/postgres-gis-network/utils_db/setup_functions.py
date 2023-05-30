import psycopg2
import os

from psycopg2 import sql
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(script_dir, '../.env')
load_dotenv(env_path)   # take environment variables from .env.

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

def get_db_connection(dbname, host, port):

    try:
        # create a new database connection by calling the connect() function
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        print("Connection successful")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed to connect to the database: ", error)
        conn = None

    return conn

def create_schema(dbname, host, port, schema):
    conn = get_db_connection(dbname, host, port)
    if conn is not None:
        try:
            #  create a new cursor
            cur = conn.cursor()

            # execute the CREATE SCHEMA statement
            cur.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema)))

            # commit the transaction
            conn.commit()
            print("Schema created successfully")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                # close the cursor with the PostgreSQL
                cur.close()
                # close the connection with the PostgreSQL
                conn.close()
                print("PostgreSQL connection is closed")