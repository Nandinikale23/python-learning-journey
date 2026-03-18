'''Can you change the self parametr inside a class to something else(say"nandini")
try changing self to "slf" or "nandini" and see the effects'''


class Employee:
    lang = "python" # class attribute
    salary = 130000 # class attribute 
    
    def getinfo(nandini):
        print(f"the lang is {nandini.lang}. th salary is {nandini.salary} . age is {nandini.age}")
    
    
        
        
Nan = Employee()
Nan.age= 21 # instance attribute
Nan.lang= "html" # instance attribute
Nan.getinfo() #eqivalent to Employee.getinfo(Nan)


# we can change self to nandini or also slf