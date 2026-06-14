''' WAP to mine a file and find out whether it contains "python" '''

with open("pb_06file.txt") as f:
    content = f.read()
    
if("python" in content):
    print("yes python is present")
else:
    print("no python is not present ")