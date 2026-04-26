#filter():= Used to select only matching values(True condition)

list1=[2,3,4,5,22]

def fun(a):
    return a>3

new_list= list(filter(fun,list1))
print(new_list)


#using lambda function 
l=[1,2,3,4]
result= list(filter(lambda x:x%2==0,l))
print(result)
