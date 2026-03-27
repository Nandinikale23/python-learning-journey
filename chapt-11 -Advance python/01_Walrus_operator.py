'''✅ Walrus Operator (:=) allows assigning a value to a variable while using it in an expression in the same line.'''

'''Without walrus 
 Example
n = len("hello")
print(n)'''

#using walrus 
print(n:=len("hello"))



''' Without Walrus 
   name = input("Enter name: ")
   if len(name) > 5:
      print("Long name")'''
      
#using walrus
if(name:= input("enter name: ")) and len(name)> 5:
    print("long name")