#private(__var):=   "__"use to create private and only inside the class can not accessed outside the class




class Student:
    def __init__(self,name,age,salary):
        self.name= name
        self.age= age
        self.__salary= salary      # make private
        
    def agefind(self):
        return self.age
    
    def getsalary(self):
        print(self.__salary)     #called inside class
        

s1= Student("nandini", 21, 40000)
s1.getsalary()  #it works



#another method to read private data
print(s1._Student__salary)  #output is 40000
