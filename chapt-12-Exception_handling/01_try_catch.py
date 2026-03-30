try:       #risky code
    a= int(input("hey, enter a number:"))
    print(a)
    
except Exception as e:              #error handling
    print(e)
    
print("thank you")  #after exception handling program not stop so print "thank you"
    