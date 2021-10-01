from Models.Group import Group
from Models.Student import Student
from Models.Teacher import Teacher
from Models.Subject import Subject
from Functions.Menu import Menu
from Functions.Create import Create
from Functions.Delete import Delete
from Functions.Read import Read
from Database.BaseModel import db
from MainLoopLogic.create_db import create_db
from MainLoopLogic.main_loop import main_loop
from peewee import *

if __name__ == '__main__':
    create_db()
    main_loop()



