'''class method:= It works with the class, not with the object.
                  **self → refers to object
                  **cls → refers to class'''
                  

class Student:
    name = "Nandini"
    @classmethod
    def show(cls):
        print(f"the student name is {cls.name}")
        

a=Student()
a.name="rani"# instance attribute not shown because we use classmethod to acces class 
a.show()