'''create a class with a class attribute a ;
   create an object from it and set 'a' and 
   directly using object a=0 
   does this change the class attrubute?'''
   
   
   
class Demo:
    a=5
    
obj=Demo()
obj.a=0 
print(obj.a) #print 0 