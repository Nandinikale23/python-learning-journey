#WAP to fill in a letter tempate given below with name and date
'''letter= Dear<|name|>,
        you are selected!
        <|Date|>'''
        

letter= '''Dear <|Name|>,
        you are selected!
        <|Date|>'''
        
print(letter.replace("<|Name|>","nandini").replace("<|Date|>","13 agust 2003"))