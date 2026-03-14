'''create class "programmer" for storing information of few programmers working at microsoft'''


class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,age):
        self.name= name  
        self.salary= salary
        self.age = age
        
obj=Programmer("nandini",120000,21)
print(obj.name,obj.salary,obj.age, obj.company)
obj1=Programmer("rudra",130000,20)
print(obj1.name,obj1.salary,obj1.age,obj.company)
obj2=Programmer("Sakshi",10000,20)
print(obj2.name,obj2.salary,obj2.age,obj.company)
