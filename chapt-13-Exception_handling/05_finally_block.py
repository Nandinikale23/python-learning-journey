'''finally:= finally always runs (error or not)'''

try:
    a=int(input("enter a number: "))
    print(a)
    
except:
    print("error")
    
finally:
    print("always runs")