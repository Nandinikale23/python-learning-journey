'''1)dict merge operator(|):= 👉 | is used to combine two dictionaries
   2)Dictionary Update Operator (|=):= is used to update existing dictionary'''
   
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

d3 = d1 | d2
print(d3)


#update dict operator
d6= {"a": 1, "b": 2}
d7 = {"c": 3}

d6 |= d7
print(d6)