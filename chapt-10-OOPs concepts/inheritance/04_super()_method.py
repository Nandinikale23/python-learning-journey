'''Super()method:= call parent class method inside child class. 
                   👉 It means:“Go to my parent class and use its function.”'''




class Employee:
    company = "Google"
    def aboutEmp(self):
        print(f"the comapny name of all employees is {self.company}")
        
class Tester(Employee):
    work="testing"
    def abouttester(self):
        super().aboutEmp() #calling parent method 
        print(f"tester works {self.work}")
        
class devlopers(Tester):
    works= "devlopement"
    def aboutdevloper(self):
        super().abouttester()  #calling its parent method 
        print(f"the work of devloper is {self.works} ")
        
a = Employee()
b= Tester()
c= devlopers()


c.aboutdevloper()


     
 