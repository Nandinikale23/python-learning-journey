class Student:
    def info(self,name=None):
        if name is None:
            print("no name")
        else:
            print("name: ", name)
        
s= Student()
s.info()
s.info("Nandini")