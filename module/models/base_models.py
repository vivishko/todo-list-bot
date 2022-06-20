"""
    Parent-classes
"""

import os
from peewee import Model
from peewee import PostgresqlDatabase


db = PostgresqlDatabase(database=os.getenv("DATABASE"), user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"), host=os.getenv("HOST"), port=os.getenv("PORT"))


def get_database():
    return db


class BaseModel(Model):
    """ Basic class, used for tables-classes in /module/base_models.py """
    class Meta:
        database = get_database()


class Singleton:
    """ Singleton realisation for database connection class in /module/dbhelper.py """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# timestamp field with timezone class
'''
class TimestampTzField(Field):
    """ A timestamp with timezone by serializing the value with isoformat. """
    field_type = 'TEXT'  # This is how the field appears in Sqlite
    def db_value(self, value: datetime) -> str:
        if value:
            return value.isoformat()
    def python_value(self, value: str) -> str:
        if value:
            return datetime.fromisoformat(value)
'''