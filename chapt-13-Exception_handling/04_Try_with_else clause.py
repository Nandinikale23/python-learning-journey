'''Else := else runs only if no error'''

try:
    a= int(input("enter a number: "))
    print(10/a)
    
except:
    print("error")
    
else:
    print("no error occures")