from Models.Group import Group
from Models.Student import Student
from Models.Teacher import Teacher
from Models.Subject import Subject

class Read:

    @staticmethod
    def read_all_student():
        for student in Student.select():
            print(
                f"ФИО студента: {student.fio}\n"
                f"Номер группы: {student.group_num}\n"
                f"---------------------------------------------------------"
            )

    @staticmethod
    def read_all_group():
        for group in Group.select():
            print(
                f"Кол-во студентов: {group.amount}\n"
                f"Номер группы: {group.group_num}\n"
                f"Куратор группы: {group.teacher.name}\n"
                f"---------------------------------------------------------"
            )

    @staticmethod
    def read_all_teacher():
        for teacher in Teacher.select():
            print(
                f"ФИО преподавателя: {teacher.name}\n"
                f"Предмет, который ведёт: {teacher.subject.name}\n"
                f"---------------------------------------------------------"
            )

    @staticmethod
    def read_all_subject():
        for subject in Subject.select():
            print(
                f"Название предмета: {subject.subject_name}\n"
                f"---------------------------------------------------------"
            )