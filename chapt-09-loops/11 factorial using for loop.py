#factorial of 5 is 5!=1*2*3*4*5

n= int(input("enter number to calculate factorial:"))
product=1
for i in range(1,n+1):
    product = product * i
    
print(f"the factorial {n} is {product}")