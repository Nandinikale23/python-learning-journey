#When a child class changes the method of parent class, it is called method overriding.


class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

'''Parent class already has: sound()

But child class creates same method again with different behavior.

So child method replaces parent method.

This is called method overriding.'''