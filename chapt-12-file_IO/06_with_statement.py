#without with statement we write code it requires f.close() means file close like this:

f= open("file.txt.txt")
print(f.read())
f.close()


'''the same code can be written using with statement 
  it does not needs f.close() with statement automatically close file'''
  
with open("file.txt.txt") as f:
    print(f.read())
    

