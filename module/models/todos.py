import datetime
from peewee import *

from module.models.base_models import BaseModel
from module.models.users import User


class ToDo(BaseModel):
    """ A model of to-do's table """
    action_id = TextField(column_name="action_id", primary_key=True)
    user_id = ForeignKeyField(User, backref="to_dos")
    created_at = DateTimeField(column_name="created_at", default=datetime.datetime.now)  #, utc=True)
    to_do_at_day = TextField(column_name="to_do_at_day", null=True)
    to_do_at_time = TextField(column_name="to_do_at_time", null=True)
    action = TextField(column_name="action", null=True)
    description = TextField(column_name="description", null=True)

    def __str__(self):
        return f"user_id: {self.user_id}, action_id: {self.action_id}"
