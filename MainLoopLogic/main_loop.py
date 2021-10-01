from Models.Group import Group
from Models.Teacher import Teacher
from Models.Student import Student
from Models.Subject import Subject
from Functions.Menu import Menu
from Functions.Create import Create
from Functions.Read import Read
from Functions.Delete import Delete
from peewee import *


def main_loop():
    while True:
        groups = [group.group_num for group in Group.select()]
        subjects = [subject.subject_name for subject in Subject.select()]
        teachers = [teacher.name for teacher in Teacher.select()]


        Menu.main_menu()
        try:
            choice = int(input("Ваш выбор?"))
        except ValueError:
            print("Ошибка ввода. Введите число от 1-13")
            continue

        if choice == 1:
            fio = str(input("Введите ФИО студента: "))
            print("Выберите группу из имеющихся: ", end='')
            print(' '.join([str(group) for group in groups]))
            group_number = int(input("Введите номер группы: "))
            try:
                Create.create_student(fio, group_number)
                print("Студент создан!")
            except IntegrityError:
                print(f"Данной группы не существует, выберите из имеющихся или добавьте её: ", end="")
                print(' '.join([str(group) for group in groups]))

        elif choice == 2:
            fio = str(input("Введите ФИО: "))
            print("Выберите предмет из имеющихся: ", end='')
            print(' '.join([str(subject) for subject in subjects]))
            subject_teacher = str(input("Введите предмет, который ведет преподаватель: "))
            try:
                Create.create_teacher(fio, subject_teacher)
                print("Преподаватель создан!")
            except IntegrityError:
                print(f"Данного предмета не существует, выберите из имеющихся или добавьте его: ", end="")
                print(' '.join([str(subject) for subject in subjects]))

        elif choice == 3:
            amount = int(input("Введите кол-во человек в группе: "))
            group_number = int(input("Введите номер группы: "))

            print("Выберите преподавателей из имеющихся: ", end="")
            print(' '.join([str(teacher) for teacher in teachers]))
            teacher = str(input("Введите ФИО преподавателя: "))
            try:
                Create.create_group(amount, group_number, teacher)
                print("Группа создана!")
            except IntegrityError:
                print(f"Данного преподавателя не существует, выберите из имеющихся или добавьте его: ", end="")
                print(' '.join([str(teacher) for teacher in teachers]))

        elif choice == 4:
            subject_name = str(input("Введите название предмета: "))
            Create.create_subject(subject_name)
            print("Предет создан!")

        elif choice == 5:
            Read.read_all_student()

        elif choice == 6:
            Read.read_all_teacher()

        elif choice == 7:
            Read.read_all_group()

        elif choice == 8:
            Read.read_all_subject()

        elif choice == 9:
            students = [student.fio for student in Student.select()]
            print("Выберите студентов из имеющихся: ", end="")
            print(' '.join([str(student) for student in students]))
            name = str(input("Введите ФИО студента, которого хотите удалить: "))
            try:
                Delete.delete_student(name)
            except:
                print("Данного студента не существует, попробуйте еще раз")


        elif choice == 10:
            print("Выберите преподавателей из имеющихся: ", end="")
            print(' '.join([str(teacher) for teacher in teachers]))
            fio = str(input("Введите ФИО преподавателя, которого хотите удалить: "))
            try:
                Delete.delete_teacher(fio)
            except:
                print("Данного преподавателя не существует, попробуйте еще раз")


        elif choice == 11:
            print("Выберите группу из имеющихся: ", end='')
            print(' '.join([str(group) for group in groups]))
            group_number = str(input("Введите номер группы, которую хотите удалить: "))
            try:
                Delete.delete_group(group_number)
            except:
                print("Данной группы не существует, попробуйте еще раз")


        elif choice == 12:
            print("Выберите предмет из имеющихся: ", end='')
            print(' '.join([str(subject) for subject in subjects]))
            subject_name = str(input("Введите название предмета, который хотите удалить: "))
            try:
                Delete.delete_subject(subject_name)
            except:
                print("Данного предмета не существует, попробуйте еще раз")


        elif choice == 13:
            db.close()
            break

        else:
            continue

        continue_choice = int(input("1-Продолжить\n2-Выйти"))
        if continue_choice == 1:
            continue
        else:
            db.close()
            break