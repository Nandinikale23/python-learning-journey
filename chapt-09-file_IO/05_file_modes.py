# r= open for reading 
# w= open for writing 
# a= open for appending 
# + = open for updating
# r+ = read and write 
# w+ = write and read
# a+ = append and read
# 'rb' will open for read in binary mode.  
# 'rt' will open for read in text mode




#append mode 

st = " hey hellow !"
f= open("myfile.txt","a")
f.write(st)
f.close()   #check o/p in myfile.txt 