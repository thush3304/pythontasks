class Student:

    def __init__(student, name, age, class_):
        student.name = name
        student.age = age
        student.class_ = class_ 
    def grade(score1, score2, score3):
        total = score1 + score2 + score3
        avg = (total/300)*100
        return avg
       

name = Student(input("Enter your name:"), input("Enter your age:"), input("Enter your class:"))
print(getattr(name, "name", "age"))



