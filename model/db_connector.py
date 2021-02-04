import mysql.connector as connector
from mysql.connector import Error
from config import login

'''
Script used to connect, make queries and disconnect to the mysql database
'''

class MysqlDB():

    def __init__(self):
        self.__conn = None
        self.__database_name = login['database']
        self.__host = login['host']
        self.__user = login['user']
        self.__password = login['password'] 
        self.__connect()

    def __use_db(self):
        try:
            stmt = self.__conn.cursor()
            stmt.execute(f"USE {self.__database_name}")
            print(f"Using database {self.__database_name}")

        except Error as e:
            print(e)

    def __connect(self):
        try:
            self.__conn = connector.connect(
                host=self.__host, user=self.__user, password=self.__password)

            if self.__conn.is_connected():
                print(f"Connected to mySQL")
                self.__use_db()

        except Error as e:
            print(e)

    def execute_select_query(self, query):
        """Used when a select query is needed, returns the data from query
        """
        stmt = self.__conn.cursor()
        stmt.execute(query)
        db_return = stmt.fetchall()
        return db_return
    
    def execute_query(self, query):
        """Used to update or modify the database, query is commited
        """
        stmt = self.__conn.cursor()
        stmt.execute(query)
        self.__conn.commit()
        print("Database updated")
        
    def disconnect(self):
        """Disconnect from the mysql database
        """
        if self.__conn is not None and self.__conn.is_connected:
            self.__conn.close()
            print(f"Connection to database {self.__database_name} is closed.")
