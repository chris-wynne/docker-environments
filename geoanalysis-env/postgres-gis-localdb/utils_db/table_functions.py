import csv
import psycopg2
from psycopg2 import sql
from setup_functions import get_db_connection

def create_table_from_csv(dbname, host, port, schema, table_name, csv_file_path):
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