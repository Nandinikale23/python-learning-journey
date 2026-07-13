#You create your own error message, Custom exception = user-defined error
#Custom Exception = your own rule + your own error

#create custom exception
class AgeError(Exception):
    pass    
#use it
try:
    age = int(input("Enter age: "))
    
    if age < 18:
        #raise custom exception
        raise AgeError("You are underage")
    
    print("Eligible")

#handle 
except AgeError as e:
    print(e)