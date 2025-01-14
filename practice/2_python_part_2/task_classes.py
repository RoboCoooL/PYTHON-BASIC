"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


class Homework:
    def __init__(self, text, deadline: datetime.timedelta, created: datetime.datetime):
        self.text = text
        self.deadline = deadline
        self.created = created
        self.is_done = False

    def is_active(self):
        return self.created + self.deadline > datetime.datetime.today() or self.is_done


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    def do_homework(self, hw: Homework) -> Homework:
        if hw.is_active():
            hw.is_done = True
            return hw
        else:
            print('You are late')
            return None


class Teacher(Person):
    def create_homework(self, text, days_to_compete) -> Homework:
        new_hw = Homework(text, datetime.timedelta(days=days_to_compete), datetime.datetime.today())
        return new_hw


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name = 'Petrov'  # Daniil
    student.first_name = 'Daniil'  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(f"{expired_homework.created.ctime() = }")  # Example: 2019-05-26 16:44:30.688762
    print(f"{expired_homework.deadline.days = }")  # 0:00:00
    print(f"{expired_homework.text = }")  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(f"{oop_homework.deadline.days = }")  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
