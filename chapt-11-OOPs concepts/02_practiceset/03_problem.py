'''create class employee and add salary and increment properties to it
   write method salaryafterincrement method with @property decorator
   with a setter which changes value of increment based on the salary '''

class Employee:
    salary= 234
    increment=20
    @property
    def salaryafterincrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary) -1)*100
        
    
e= Employee()
e.salaryafterincrement = 280.8
print(e.increment)
    