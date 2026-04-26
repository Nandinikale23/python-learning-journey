#higher_order_function:= function take another function as a argument 

#map():= apply function to every element 


def cube(a):
    return a*a*a

print(cube(2))
list1=[1,2,3,4,5]

new_list= list(map(cube,list1)) # usign map function apply to every element in list
print(new_list)



#using lambda function with map

nums=[5,2,3]
result= list(map(lambda x:x*2,nums))
print(result)
