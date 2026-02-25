''' repeat program 4 for a list of such words to be censored'''

words=["donkey","bad","big"]

with open("pb_04file.txt") as f:
    content= f.read()

for word in words:
    content = content.replace(word,"#####")
    

with open("pb_04file.txt","w") as f:
     f.write(content)