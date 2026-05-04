#Public variable = normal variable, It can be accessed from anywhere 


class Student:
    def __init__(self):
        self.name = "Nandini"   # public variable

s1 = Student()

print(s1.name)   # works (outside class)