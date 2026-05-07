#Encapsulation:= Encapsulation means wrapping data and methods into a single unit.
              #hiding internal details of how object works and only showing output. it is mainly used fro data protection. 
            

class Student:
    
    def __init__(self):
        self.__marks = 0   # private variable (hidden)
    
    # method to set marks
    def set_marks(self, m):
        if m >= 0:
            self.__marks = m
        else:
            print("Invalid marks")
    
    # method to get marks
    def get_marks(self):
        return self.__marks


# create object
s = Student()

# set marks
s.set_marks(90)

# get marks
print(s.get_marks())