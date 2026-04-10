#WAP which finds out whether a given name is present in a list or not 

list=["neha","rohan","onkar","bhushan"]
name=input("enter your name:")

if(name in list):
    print("your name is in the list")
else:
    print("your name is not in list")