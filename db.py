import mysql.connector as connector
from mysql.connector import Error

database_name = 'Guld'

def use_db(conn):
    try:
        stmt = conn.cursor()
        #stmt.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        stmt.execute(f"USE {database_name}")
        print(f"Using {database_name}")

    except Error as e:
        print(e)

def get_companies(conn):
    stmt = conn.cursor()

    get_company = "Select * from company"
    stmt.execute(get_company)

    comp = stmt.fetchall()
    print(comp[0])

def connect():
    conn = None  # mySQL connector
    try:
        conn = connector.connect(
            host="localhost", user="root", password="hondansr")

        if conn.is_connected():
            print(f"Connected to mySQL")
            use_db(conn)
            get_companies(conn)

    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close()
            print("Connection is closed.")

if __name__ == "__main__":
    connect()