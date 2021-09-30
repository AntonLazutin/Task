from Models.Group import Group
from Models.Student import Student
from Models.Teacher import Teacher
from Models.Subject import Subject

class Delete:


    @staticmethod
    def delete_group(group_num):
        group = Group.get(Group.group_num == group_num)
        group.delete_instance()

    @staticmethod
    def delete_student(fio):
        student = Student.get(Student.fio == fio)
        student.delete_instance()

    @staticmethod
    def delete_teacher(name):
        teacher = Teacher.get(Teacher.name == name)
        teacher.delete_instance()

    @staticmethod
    def delete_subject(subject_name):
        subject = Subject.get(Subject.subject_name == subject_name)
        subject.delete_instance()