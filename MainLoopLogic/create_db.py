from Database.BaseModel import db
from Models.Student import Student
from Models.Subject import Subject
from Models.Group import Group
from Models.Teacher import Teacher
import peewee


def create_db():
    db.connect()
    try:
        db.create_tables([Student, Group, Subject, Teacher])
    except peewee.OperationalError:
        pass
