#Protected (_var):= Not strictly private, can access outside class but should not be accessed directly.

class Student:
    def __init__(self):
        self._age = 21   # protected

s1 = Student()
print(s1._age)   # works, but not recommended and should not be access