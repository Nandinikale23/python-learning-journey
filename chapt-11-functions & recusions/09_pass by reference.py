#pass by reference: orignal value pass 
# muttable datatypes :list,dictonary,set,boolean

my_list =[1,2,4]

def modify_list(li):
    li.append(5)
    print(li)
    
print("before calling function",my_list)

modify_list(my_list)

print("after calling function",my_list)