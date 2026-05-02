'''create a class 'pets' from a class 'animal' and furthur create a class 'dog' 
   from 'pets' add a method 'bark' to a class 'dog' '''
   

class animal:
    type ="dogs"
    def types(self):
        print(f"the animal type is {self.type}")

    
        
class pets(animal):
    colour = "black"
    def show(self):
        print(f"te pets colour is {self.colour}")
        
class dog(pets):
    size = "small"
    def about(self):
        print(f"the type of dog is {self.size}")
        
    def bark(self):
        print("Dog is barking: Woof Woof!")

        

a= animal()
a.types() 

b=pets()
b.show()

c= dog()
c.about()
c.bark()
     
        