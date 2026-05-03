'''static method:= its same as class method but it has no access of class and object'''
 
 
class Static:
    category = "student"
    standard = "TE" 
    department ="IT" 
    
    @staticmethod #decorators to mark greet as static method 
    def greet():
        print("hellow students, good morning") 
        
    
    def getinfo(self):
        print(f" category is {self.category}. standard is {self.standard}. dept is {self.department}")  
        
        

nandini = Static()
nandini.greet()
nandini.getinfo()