from peewee import *

db = SqliteDatabase('iCodeTask.db')

class BaseModel(Model):

    class Meta:
        database = db
        order_by = "Id"