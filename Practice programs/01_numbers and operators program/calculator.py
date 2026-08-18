a= float(input("Enter value of a: "))
b= float(input("Enter value of b: "))

operator = input("enter operator(+,-,*,/): ")

if operator == "+":
    print("result",a+b)
elif operator == "-":
    print("result", a-b)
elif operator == "*":
    print("result",a*b)
elif operator == "/":
    print("result",a/b)
else:
    print("invalid operator")    