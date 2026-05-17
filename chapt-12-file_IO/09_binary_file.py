#Binary file:= stores data in o and 1 format
#modes:= rb= read binary, write binary
#use b means byte means it indicates data is binary without byte its text


#write binary data
with open("data.bin","wb") as f:
    f.write(b"hellow, how are you")
    

#read binary file
with open ("data.bin","rb") as f:
    data=f.read()
    print(data) 
    

#pickle:= Pickle is used to save Python objects into a file and later load them back

#1.save data(dump)
import pickle
data={"name": "nandini", "age":21}

with open("data.pkl","wb") as f:
    pickle.dump(data,f) #save object
    #dump():= store data in file
    

#load data(get back)
import pickle
with open("data.pkl","rb") as f:
    data=pickle.load(f)
print(data)