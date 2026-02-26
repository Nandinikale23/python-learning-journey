with open("pb_08file.txt") as f:
    content = f.read()
    
with open("pb_08file_copy.txt","w") as f:
    f.write(content)
    
    
# create new file pb_08file.txt and copy the content from pb_08file.txt 