#reduce():= Used to reduce list to single value
          # “Combine all values into one”
          
          
from functools import reduce

nums= [1,2,3,3,4]

def fun(a,b):
    return a+b

result = reduce(fun,nums)
print(result)


#using lambda function
list= [2,3,1,1,3]

answer = reduce(lambda x,y: x+y, list)
print(answer)