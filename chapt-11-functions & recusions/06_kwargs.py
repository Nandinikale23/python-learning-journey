#kwargs:= you can pass many values in key= values form 
       # it stores data as dictonary 
       
       
def display_info(**kwargs):
    print(kwargs)
    
    for key,value in kwargs.items():
        print(key,"->",value)
        
display_info(name="nandini",age=21,city="pune")   