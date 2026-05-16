#JSON file:= javascript object notation, 
           #json is a format it used to saved dictionary data in file format, used in websites,apis
           #it looks like python dictionary
           

#write Json file
import json
data={
    "name":"Nandini",
    "age":21
} 

with open("data.json","w") as f:
    json.dump(data,f) #convert dict into json file  
    
    

#read json file
import json

with open("data.json","r") as f:
    data=json.load(f)  #read file into dictionary
    
print(data["name"])



#convert without file

#1.python into json string
import json
data={"name":"nandini"}
json_data=json.dumps(data)
print(json_data)


#2.json into python
import json
json_data='{"name":"Nandini"}'
data=json.loads(json_data) 
print(data["name"])   