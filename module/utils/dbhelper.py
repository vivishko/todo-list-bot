"""
    Creating database connection class (singleton pattern)
"""

import os
import sys
from peewee import *
from psycopg2 import Error

from module.models.base_models import Singleton


class DBConnection(Singleton):
    """ An object of database connection """
    connection = None
    curs = None

    def __init__(self):
        self.database = os.getenv("DATABASE")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.connection = None
        self.curs = None

    def __str__(self):
        return 'Database connection object'

    def get_connection(self):
        """ Creating PostgreSQL's database connection """
        if self.connection is None:
            try:
                self.connection = PostgresqlDatabase(self.database, user=self.user, password=self.password,
                                                     host=self.host, port=self.port)
                self.curs = self.connection.cursor()
            except (Exception, Error) as error:
                print("PostgreSQL's connection error: \n", error)
                sys.exit(1)
        return self.connection

    def __del__(self):
        """ Closing database connection """
        if self.connection is not None:
            self.curs.close()
            self.connection.close()
        print("PostgreSQL's connection closed.")

# database connection
'''
connection = None
try:
    connection = PostgresqlDatabase(os.getenv("DATABASE"),
                                  user=os.getenv("USER"),
                                  password=os.getenv("PASSWORD"),
                                  host=os.getenv("HOST"),
                                  port=os.getenv("PORT"))
    curs = connection.cursor()
    # import json
    # print("\nPostgreSQL server info: \n", json.dumps(connection.get_dsn_parameters(), indent=4), "\n")
    # curs.execute("SELECT version();")
    # record = curs.fetchone()
    # print("You are connected to ", record, "\n")
    print("Connected! ")
    # import models
    # models.User.create(user_id='1-Qwerty', username='vivishko', phone='89875197310')
    # models.ToDo.create(action_id='frwod', user_id='1-Qwerty', to_do_at_day='4', to_do_at_time='NULL',
    #  action='bot release', description='NULL')

except (Exception, Error) as error:
    print("PostgreSQL's connection error: \n", error)
    # from time import sleep
    # sleep(2)
    sys.exit(1)
finally:
    if connection:
        curs.close()
        connection.close()
        print("PostgreSQL's connection closed")
'''