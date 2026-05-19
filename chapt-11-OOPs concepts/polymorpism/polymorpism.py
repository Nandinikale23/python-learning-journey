#polymorpism:= one thing can work in many forms
#one method, function, or operator can perform different actions depending on the object 


class Cat:
    def sound(self):
        print("meow")

class dog:
    def sound(self):
        print("bark")

d= dog()
c= Cat()

d.sound() 
c.sound()