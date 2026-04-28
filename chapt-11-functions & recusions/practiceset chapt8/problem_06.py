#WAP python function to remove a given word from a list ad stript it at the same time .


#only remove an from list l
def rem(l,word):
    for item in l:
        l.remove(word)
        return l


l=["nandini", "rohan", "Shubham", "an"]

print(rem(l,"an"))
#output is ["nandini","rohan","shubham"]




#remove an from all words in list means using strip function.
  #strip(): it remove any word from starting and ending in list like rohan we want to remove "an" so o/p is roh
  
def remo(list,word):
    n=[]
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
            
list=["Nandini"," shubham", "rohan", "Nishan","an"]

print(remo(list,"an"))

#output is ["Nandini","shubham","roh","nish"]