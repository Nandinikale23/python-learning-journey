'''WAP class"Train" which has methods to book a ticket, 
   get status (no of seats)and get fare information of Train which has methods to book a ticket,
   get fare information of train running under indian railways'''
   

from random import randint
   
class Train:
    def book_ticket(self, train_no, fro, to):
        print(f"ticket is boked in train_no :{train_no} from {fro} to {to}")
        
    def getstatus(self, train_no):
        print(f"tain no : {train_no} is running on time")
        
    def getfare(self, train_no,fro, to):
        print(f"ticket fare in train_no : {train_no} from {fro} to {to} is {randint(222,5555)}")
        
        
obj=Train()
obj.book_ticket(1239,"delhi","pune")
obj.getstatus(1239)
obj.getfare(1239,"delhi","pune")
        
        
        