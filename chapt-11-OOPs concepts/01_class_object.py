#class:= class is blueprint of creating object 
       # class is collection of objects
       #class first letter is always capital
       
       
#object:= object is a instance of class
        # object is think like real world thing 
        
class Person:
    pass

obj=Person()
print(type(obj))
print(obj)  #it gives address of object in output


class Employee:
    lang = "py" # this is class attributes
    salary= 200000
    

em1= Employee() # create obj 
em1.name="nandini" # this is an instance attribute
print(em1.name,"\n", em1.lang,"\n", em1.salary)



em2 =Employee()
em2.name="rudra"  # this is an instance attribute
print(em2.name, "\n", em2.salary, "\n", em2.lang)



