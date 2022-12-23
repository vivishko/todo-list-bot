"""
    Parent-classes
"""
from peewee import Model
from module.utils.database_helper import db

class BaseModel(Model):
    """ Basic class, used for tables-classes in /module/models/base_models.py """
    class Meta:
        # database = get_database()
        database = db


# singleton base class for database connection, not used, because peewee has own singleton realisation

# class Singleton:
#     """ Singleton realisation for database connection class in /module/utils/database_helper.py """
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance


# timestamp field with timezone class, not used, because peewee has own class

# class TimestampTzField(Field):
#     """ A timestamp with timezone by serializing the value with isoformat. """
#     field_type = 'TEXT'  # This is how the field appears in Sqlite
#     def db_value(self, value: datetime) -> str:
#         if value:
#             return value.isoformat()
#     def python_value(self, value: str) -> str:
#         if value:
#             return datetime.fromisoformat(value)
