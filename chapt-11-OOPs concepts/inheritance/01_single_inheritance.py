'''Inheritance: inheritance is a way of creating a new class from an existing class '''
'''One class aquiring the properties from other class '''

#types of inheritance
#1.single inheritance
#2.multiple inheritance
#3.multilevel inheritance



#1.single inheritance
class Employee:
    company = "TCS"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
class Programmer(Employee):
    name = "Rahul"

    
a = Employee()
b = Programmer()

print(a.company,b.company,b.name)

    
    

    