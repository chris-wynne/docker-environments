import csv
import psycopg2
from psycopg2 import sql
from setup_functions import get_db_connection

def query_data(dbname, host, port, query):
    conn = get_db_connection(dbname, host, port)
    try:
        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)