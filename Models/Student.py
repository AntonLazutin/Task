from Database.BaseModel import BaseModel
from .Group import Group
from peewee import *

class Student(BaseModel):
    id = PrimaryKeyField(null=False, column_name="Id")
    fio = TextField(null=True, column_name="FIO")
    group_num = ForeignKeyField(Group, backref="students", on_delete="CASCADE",
                                column_name="Group", to_field='group_num')

    class Meta:
        db_table_name = "Student"
