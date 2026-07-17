'''Advanced type hints are used for complex data like list, dictionary, functions, etc.'''


from typing import list, tuple, dict, union , set

#list of integers
num : list[int]= [1,2,3,4,5]

#tuple of a string and an integer 
person : tuple[str,int]= ("nandini", 40)

#dictonary with string keys and integer values 
scores : dict[str, int ] = {"nandini ": 33 , "rudra": 22}

#union type for variables that can hold multiple types 
identifier: union[int,str]= "ID333"
identifier = 123455 # also valid 


# set with integers
s: set[int]= {1,2,3,4}

#function type hint
def add(a: int, b: int) -> int:
    return a+b 