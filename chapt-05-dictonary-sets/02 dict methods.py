marks={"nandini":98,
       "rudra":99,
       "saburi":97,
       "ranvir":99,
       0:"sakshi"}

#methode1 items():returns list of (key,value)in tuple form
print(marks.items())

#methode2 keys():returns list list of key's
print(marks.keys())

#method3 values():returns list of values
print(marks.values())

#methode4 update():
marks.update({"nandini":"sam"})
print(marks)

#methode5 get():returns value of specific keys
print(marks.get("nandini")) # o/p= sam beacause we have update dic

#method6 len()
print(len(marks))

#print(marks.get("shivani")) ---- prints none beacause shivani is not in dic
#print(marks["shivani"])----- returns error 


#adding 1 dict in another dict using update()
f1={"banana":"yellow",
    "apple":"red"}
s1={"parrot":"green"}
f1.update(s1)
print(f1)

#remove element in dict
     #pop():specific key:value dlt 
     #popitem():last dlt
     #del keyword:
     #lear():all clear provide empy dict
     
#1. pop()
city={"pune":10,"nashik":8,"latur":5,"bid":6}
city.pop("pune")
print(city)

#2.popitem()
city.popitem()
print(city)

#del 
del city['latur']
print(city)

#clear()
city.clear()
print(city)