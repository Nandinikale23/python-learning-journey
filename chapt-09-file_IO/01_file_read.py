'''file:= file is data stored in storage device .
         types of file:= 1. text file = .txt
                         2. binary file= .jpg, .dat '''
                         


f = open("file.txt.txt", "r")
print(f.read())
f.close() # run in folder terminal using:= python 01_file.py 



         #OR another way directly using full path of file directly run 
'''f = open(r"d:\pythonpract\chapt9 file_IO\file.txt.txt", "r")
data = f.read()
print(data)
f.close() '''




