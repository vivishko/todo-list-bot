import datetime
from peewee import *
# from telegram import Update
# from telegram.ext import CallbackContext
# import uuid

from module.models.base_models import BaseModel
# from module.utils.info import get_users_data_dict


class User(BaseModel):
    """ A model for client's table """
    user_id = TextField(column_name="user_id", primary_key=True)
    username = TextField(column_name="username", null=True)
    phone = TextField(column_name="phone", null=True)
    timestamp = DateTimeField(column_name="timestamp", default=datetime.datetime.now)  #, utc=True)
    utc_offset = IntegerField(column_name="utc_offset", null=True)
    timezone = TextField(column_name="timezone", null=True)

    # TODO: add location
    # longitude = FloatField(column_name="longitude", null=True)
    # latitude = FloatField(column_name="latitude", null=True)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'


    # this code is not nessesary, because we can use User.get_or_create() method
    
    # @classmethod
    # def get_user_and_created(cls, update: Update, context: CallbackContext) -> Tuple[User,bool]:
    #     """ getting User instance """
    #     # data = get_users_data_dict(update)
    #     user, created = User.get_or_create(username=cls.username, defaults={'phone': cls.phone})
    #     return user, created

    # @classmethod
    # def get_user(cls, update: Update, context: CallbackContext) -> User:
    #     u, _ = cls.get_user_and_created(update, context)
    #     return u
