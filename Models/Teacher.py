from Database.BaseModel import BaseModel
from peewee import *
from .Subject import Subject


class Teacher(BaseModel):
    id = PrimaryKeyField(column_name="Id")
    name = CharField(column_name='TeacherName', max_length=100, unique=True)
    subject = ForeignKeyField(Subject,
                              backref='teachers', column_name="SubjectTeacher",
                              on_delete="CASCADE", to_field="subject_name")

    class Meta:
        db_table = "Teacher"