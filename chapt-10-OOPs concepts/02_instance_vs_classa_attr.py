class Employee:
    lang = "py" # this is class attributes
    salary= 200000
    

em1= Employee() # create obj 
em1.lang ="html" # this is an instance attribute
print( em1.lang,"\n", em1.salary)


'''lang print html because instance attribute prefer priority first and then
class atrribut,  if instance attribute not present so direct goes to class attribute '''



""" instance atribute:= object property is for specific object
    class attribute := class property its for all objects in class"""