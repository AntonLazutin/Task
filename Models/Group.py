from .BaseModel import BaseModel
from .Teacher import Teacher
from peewee import *

class Group(BaseModel):
    id = PrimaryKeyField(null=False, column_name='Id')
    group_num = CharField(column_name="GroupNum", unique=True)
    amount = IntegerField(column_name="Amount",null=True)
    teacher = ForeignKeyField(Teacher, on_delete="SET NULL", backref='groups',
                              null=True, to_field="name", column_name="Teacher")

    class Meta:
        db_table_name = "Group"