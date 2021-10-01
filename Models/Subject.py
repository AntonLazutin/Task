from Database.BaseModel import BaseModel
from peewee import *

class Subject(BaseModel):
    id = PrimaryKeyField(null=False, column_name="Id")
    subject_name = CharField(unique=True, max_length=100, null=False)

    class Meta:
        db_table = "Subject"