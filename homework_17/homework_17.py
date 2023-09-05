# HW: DB in Python
# 1.Add models for student, subject and student_subject from previous lessons in SQLAlchemy.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    class_ = Column(String) 

    def __str__(self):
        return f'This is {self.id} student {self.name}. Age: {self.age}'

from random import randint, choice

random_names = ['Joe', 'Winston', 'Benedict', 'Andrea', 'Fillipe', 'Iria', 'Eric', 'Joan', 'Pablo', 'Brian', 'Timothy', 'Mario']
random_class = ['english', 'french', 'italian']

for _ in range(10):
    student = Student(name=choice(random_names), age=randint(18, 25), class_=choice(random_class)) 
    session.add(student)

session.commit()


# 2.Find all students` name that visited 'English' classes.

eng_class = session.query(Student).filter(Student.class_ == 'english').all()

for student in eng_class:
    print(f'Student id  {student.id}')
    print(f'Student name  {student.name}')
    print(f'Student age  {student.age}')
    print(f'Student class {student.class_}')
    print()