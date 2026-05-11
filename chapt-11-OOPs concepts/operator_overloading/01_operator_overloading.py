"operator overloading:= Same operator → different work depending on object"
'''for  eg operator is "+":= Same operator, different behavior.
                    1] "+" and different work like "+" used for add numbers 
                    2] "+" used for joins string'''
                    
                    
''' Some Important Magic Methods
| Operator | Method          |
| -------- | --------------- |
| +        | `__add__()`     |
| -        | `__sub__()`     |
| *        | `__mul__()`     |
| /        | `__truediv__()` |
| >        | `__gt__()`      |
| <        | `__lt__()`      |
'''


class Employee:
    def __init__(self, n):
        self.n=n
        
    def __add__(self, other):
        return self.n + other.n 
    
    
n1=Employee(23)
n2=Employee(3)

print(n1+n2)
    