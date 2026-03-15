'''WAP class"calculator" capable of finding square,cube, and square root of a number'''


class Calculator:
    
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f" the square is {self.n*self.n}")
    
    def cube(self):
        print(f"cube is {self.n*self.n*self.n}") 
        
    def squareroot(self):
        print(f"the squarerrot is {self.n**1/2}")
        

n= int(input("enter the valuue of n :"))
        
a =Calculator(n)
a.square()
a.cube()
a.squareroot()   