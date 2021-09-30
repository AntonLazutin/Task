from Models.Group import Group
from Models.Student import Student
from Models.Teacher import Teacher
from Models.Subject import Subject

class Create:


    @staticmethod
    def create_group(amount, group_number, teacher):
        group = Group.create(amount=amount, group_num=group_number, teacher=teacher)
        group.save()
        return group

    @staticmethod
    def create_student(fio, group_num):
        student = Student.create(fio=fio, group_num=group_num)
        student.save()
        return student

    @staticmethod
    def create_teacher(name, subject_name):
        teacher = Teacher.create(name=name, subject=subject_name)
        teacher.save()
        return teacher

    @staticmethod
    def create_subject(subject_name):
        subject = Subject.create(subject_name=subject_name)
        subject.save()
        return subject