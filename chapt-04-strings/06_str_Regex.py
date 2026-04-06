#Regex(regular expression):= it is used to find patterns in text
                           #exaple: find numbers, find words

#find Numbers
import re
text= "my number is 12345"
result= re.findall(r"\d+",text)
print(result)    # \d means digit(0-9) 
                 # + means one or more
                 

#find words 
text="hellow world"
result = re.findall(r"\w+",text)
print(result)     #\w means letter + digit + underscore

# output is ["hellow","world"]                       