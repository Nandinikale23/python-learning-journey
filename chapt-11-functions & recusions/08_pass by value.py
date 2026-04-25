#pass by value := passing copy not orignal 
#immutable datatypes: string ,tuple are pass by value

num= 5
def modify_num(num):
    num+=1
    print(num)
    
modify_num(num)
print("orignal num", num) 