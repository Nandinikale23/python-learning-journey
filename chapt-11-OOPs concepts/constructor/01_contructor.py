'''contructor is special method which automaticaly run when object is created
    - it takes self arguments and also take furthur
    - contructor initialize object '''





class Employee:
    lang = "python"
    salary = 1200000
    
    #contructor 
    #__init__()  is a dunder methode
    def __init__(self,name,lang,salary):   
        self.name= name 
        self.lang= lang 
        self.salary = salary 
        
        
obj = Employee("Nandini","css",1500000)
print(obj.name,obj.lang,obj.salary)