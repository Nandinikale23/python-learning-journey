li=["rudra",23.4,27,"shrutika","sakshi"]

#inserting methods of list

#1.append():add in end
li.append("nandini")
print(li)

#2.insert():add in specific index
li.insert(1,3340)
print(li) #3340 add in index 1

#3.extend():add list 1 in inst 2 and extending
li=["rudra",23.4,27,"shrutika","sakshi"]
l2=["good morning","hii"]
li.extend(l2)
print(li)


#Remove elements from list
    #pop()
    #pop(i)
    
#pop():remove from last
arr=[3,5,23,"nandini","rudra"]
arr.pop() # remove rydra in list
print(arr)

#pop(i):remove at index
arr=[3,5,23,"nandini","rudra"]
arr.pop(1)
print(arr)


#replace value
students=['a','b','c','d']
students[0]='f'
print(students)

students[1:4]='m','n','o'
print(students)


#handy methods
   #reverse()
   #sort()
   
#reverse()
l1=[1,4,3,2,5,]
l1.reverse()
print(l1)

#sort()
l1.sort()
print(l1)




