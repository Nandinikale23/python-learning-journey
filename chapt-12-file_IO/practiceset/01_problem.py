#wap to read text from a given file'poems.txt' and find out whether it contains the word 'twinkle'.
f= open("poems.txt")
content= f. read()
if("twinkle" in content):
    print("the word is present in the content")
else:
    print("the word twinkle is not present in the content")
    
f.close()