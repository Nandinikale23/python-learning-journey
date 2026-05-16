#CSV:= comma separated value . it is used to store data in table format 

#write CSV file in python

import csv 
import pandas as pd # to see data in table format 

with open("data.csv","w",newline="") as f:
    writer= csv.writer(f)
    
    writer.writerow(["Name","Age"])
    
    writer.writerow(["Nandini",21])
    
    
#read csv file
    
import csv
with open("data.csv","r") as f:
    reader=csv.reader(f)
        
    for row in reader:
        print(row)


#to see data in table format 
df = pd.read_csv("data.csv")
print(df)