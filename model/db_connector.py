import mysql.connector as connector
from mysql.connector import Error


class MysqlDB():

    def __init__(self):
        self.__conn = None
        self.__database_name = 'Guld'
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "hondansr"
        self.__connect()

    def __use_db(self):
        try:
            stmt = self.__conn.cursor()
            stmt.execute(f"USE {self.__database_name}")
            print(f"Using {self.__database_name}")

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

    def get_companies(self):
        stmt = self.__conn.cursor()

        get_company = "Select * from company"
        stmt.execute(get_company)

        comp = stmt.fetchall()
        return comp

    def disconnect(self):
        if self.__conn is not None and self.__conn.is_connected:
            self.__conn.close()
            print("Connection is closed.")
