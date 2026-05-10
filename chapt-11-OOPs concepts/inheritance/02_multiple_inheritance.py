#2.multiple inheritance : child class inherits from more than one parent class.


class Employee:
    company = "Google"
    department ="IT"
    def showinfo(self):
        print(f"the company name is {self.company} and employee departmet is {self.department}")
        

class Seniors:
    age= 40-70
    education = "masters"
    def aboutsenior(self):
        print(f"the education is {self.education} and age of seniors is {self.age}")
        
class Programmers(Employee,Seniors):
    branch = "technical"
    
a =Programmers()
a.showinfo()
a.aboutsenior()