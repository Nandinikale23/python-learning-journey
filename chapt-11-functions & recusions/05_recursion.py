#recursion:= is a function which calls itself.
            # it is used to directly use mathematical formula as function.
            
            

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n= int(input("enter a number :"))
print(f"the factorial of this number is:{factorial(n)}")