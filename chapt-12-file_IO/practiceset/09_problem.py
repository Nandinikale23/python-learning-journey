''' WAP to find out whether a file is identical and matches the content of another file '''

with open("pb_09file1.txt") as f:
    content1= f.read()
    
with open("pb_09file2.txt") as f:
    content2 = f.read()
    
if(content1 == content2):
    print("yes these files are identical")
    
else:
    print("no these files are not identical")