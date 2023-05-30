import os
import csv
import psycopg2
import pandas as pd
from psycopg2 import sql
from sqlalchemy import create_engine
from dotenv import load_dotenv

from .setup_functions import get_db_connection

script_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(script_dir, '../.env')
load_dotenv(env_path)   # take environment variables from .env.

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

def insert_csv_data_into_table(dbname, host, port, schema, table_name, csv_file_path):
    """
    Inserts data from a CSV file into a table in a PostgreSQL database.
    
    Args:
        dbname (str): The name of the database.
        host (str): The host address of the PostgreSQL server.
        port (int): The port number to connect to the PostgreSQL server.
        schema (str): The schema in which the table is located.
        table_name (str): The name of the table to insert data into.
        csv_file_path (str): The file path of the CSV file.
    
    Returns:
    None
    """
    # establish connection
    conn = get_db_connection(dbname, host, port)

    # create cursor object
    cur = conn.cursor()

    with open(csv_file_path, 'r') as f:
        # Skip the header row
        next(f)
        # Use schema.table_name format for table name
        cur.copy_from(f, f"{schema}.{table_name}", sep=',')

    conn.commit()

def create_postgres_table_from_dataframe(dataframe, table_name, schema_name, dbname, host, port):
    """
    Inserts data from a pandas DataFrame into a table in a PostgreSQL database.
    
    Args:
        dataframe (pandas.DataFrame): The DataFrame to be inserted into the table.
        table_name (str): The name of the table to insert data into.
        schema_name (str): The schema in which the table is located.
        dbname (str): The name of the database.
        host (str): The host address of the PostgreSQL server.
        port (int): The port number to connect to the PostgreSQL server.
        schema (str): The schema in which the table is located.
    
    Returns:
        None. The function performs the operation in-place and does not return a value.
    """

    # create the connection string
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
    )

    # convert the dataframe into SQL, replacing table if it already exists.
    dataframe.to_sql(
        table_name,
        con=engine,
        schema=schema_name,
        index=False, 
        if_exists='replace'
    )
    
def drop_table(dbname, host, port, schema, table_name):
    """
    Drops a table from a PostgreSQL database.

    Args:
        dbname (str): The name of the database.
        host (str): The host address of the PostgreSQL server.
        port (int): The port number to connect to the PostgreSQL server.
        schema (str): The schema where the table is located.
        table_name (str): The name of the table to be dropped.

    Returns:
        None
    """
    # establish connection
    conn = get_db_connection(dbname, host, port)

    # create cursor object
    cur = conn.cursor()

    # create the DROP TABLE SQL statement
    drop_table_sql = sql.SQL("""
        DROP TABLE IF EXISTS {}.{}
    """).format(
        sql.Identifier(schema),
        sql.Identifier(table_name)
    )

    # Execute the DROP TABLE statement
    cur.execute(drop_table_sql)

    # commit the transaction
    conn.commit()