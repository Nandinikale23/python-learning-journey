#Used to check if two variables refer to same object (memory)

a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True
print(a is c)      # False