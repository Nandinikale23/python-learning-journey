#WAP to find greatest of four numbers entered by the user 
dict={}
dict["a1"]=int(input("enter number by as user1:"))
dict["a2"]=int(input("enter number by as user2:"))
dict["a3"]=int(input("enter number by as user3:"))
dict["a4"]=int(input("enter number by as user4:"))
print(dict)

#a1=int(input("enter number by as user1:"))
#a2=int(input("enter number by as user1:"))
#a3=int(input("enter number by as user1:"))
#a4=int(input("enter number by as user1:"))
#print(dict)

if('a1'>'a2' and 'a1'>'a3' and 'a1'>'a4'):
    print("gretest number is a1:",'a1')

elif('a2'>'a1' and 'a2'>'a3' and 'a2'>'a4'):
    print("gretest number is a2:",'a2')

elif('a3'>'a1' and 'a3'>'a2' and 'a3'>'a4'):
    print("gretest number is a3:",'a3')

elif('a4'>'a1' and 'a4'>'a2' and 'a4'>'a3'):
    print("gretest number is a4:",'a4')

