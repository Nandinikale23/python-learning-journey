class Employee:
    
    @property
    def name(self):
        return f"{self.fname} {self.lname} {self.mname} "
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.mname=value.split(" ")[1]
        self.lname=value.split(" ")[2]
        
    
e= Employee()
e.name ="nandini santosh kale"
print(e.fname, e.mname, e.lname)



    
    