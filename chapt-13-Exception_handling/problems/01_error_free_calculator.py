try:
    num1=int(input("enter the value of number1: "))
    num2=int(input("enter the value of number2: "))
    
    op=input("select any one operator +,-,*,/ := ")
    
    if op== '+':
        print(f"the sum of two num is {num1+num2}")
    elif op=='-':
        print(f"sub is {num1 - num2 }")
    elif op=='*':
        print(f"multiplication is {num1 * num2}")
    elif op=='/':
        print(f"division is{num1/num2}")
    else:
        print("invalid operator")
        
        
except ZeroDivisionError:
    print("Erroe: it is a zero division error plz enter another number at zero place")

except ValueError:
    print("Error: its a value error plz enter valid error") 
    
finally:
    print("calculator is finished succesfully")
    