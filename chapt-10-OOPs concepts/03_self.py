class Employee:
    lang = "python" # class attribute
    salary = 130000 # class attribute 
    
    def getinfo(self):
        print(f"the lang is {self.lang}. th salary is {self.salary} . age is {self.age}")
        
        
Nan = Employee()
Nan.age= 21 # instance attribute
Nan.lang= "html" # instance attribute
Nan.getinfo() #eqivalent to Employee.getinfo(Nan)


#self := we can use the self as any other word not compulsary to use "self" word
#self means represents the current object of the class
#self means this object