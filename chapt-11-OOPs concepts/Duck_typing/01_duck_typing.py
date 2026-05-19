#duck typing means python checks the behaivour or method not the actual type of object. 
#means “If an object behaves like a duck, Python does not check whether it is actually a duck or not.”


class Fan:
    def start(self):
        print("Fan is starting")

class Car:
    def start(self):
        print("car is starting")

def begin(obj):
    obj.start()

C=Car()
F= Fan()

begin(C)
begin(F)


