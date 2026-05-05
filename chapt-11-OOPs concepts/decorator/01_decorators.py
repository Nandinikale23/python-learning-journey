'''Decorator:- is a function that takes another functio as argument and returns a function '''

def decorator(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction is completed")
    return wrapper

@decorator
def hello():
    print("executing all steps of transaction")
    
hello()