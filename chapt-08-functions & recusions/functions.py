#function:= fun is a group of statement performing a specific task 
# types of function:= 1. built in function(already present in python):= print(),len(),range()
                    #2. user defined functions(defined by the user):= we create for eg func1()


#function defination 
def avg():       #function
    a = int(input("enter your number:"))
    b = int(input("enter your number:"))
    c = int(input("enter your number:"))
    
    average = (a+b+c)/3
    print(average)
    
avg()    # function call