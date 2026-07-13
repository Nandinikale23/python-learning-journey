try:
    a=int(input("hey,enter a number: "))
    print(a)
    
except ValueError as v:       #manually created exception msg 
    print("its value error ")
    print(v)
    
except Exception as e:
    print(e)
    
print("thank you ")