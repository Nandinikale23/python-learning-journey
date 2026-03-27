'''3.multilevel inheritance: A class takes properties from a parent
 Then another class takes properties from that child
 for example:grandparent - parent - child'''
 
 
class Employee:
    company = "Google"
    def aboutEmp(self):
        print(f"the comapny name of all employees is {self.company}")
        
class Tester(Employee):
    work="testing"
    def abouttester(self):
        print(f"tester works as {self.work}")
        
class devlopers(Tester):
    works= "devlopement"
    def aboutdevloper(self):
        print(f"the work of deloper is {self.works} ")
        
a = Employee()
b= Tester()
c= devlopers()


b.abouttester()
b.aboutEmp()
c.abouttester()
c.aboutdevloper()
c.aboutEmp()
     
 