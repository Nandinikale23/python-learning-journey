'''
the game() function in a program lets a user play game and returns the score as an integer. 
you need to read file "hi-score.txt" which is eithe blank or contains the previous hi-score. 
you need to write a program to update the hi-score whenever the game()function breaks the hi-score.
'''

import random
 
def game():
    print("you are playing game ....")
    score= random.randint(1,62)
    #fetch the hiscore
    
    with open("hiscore.txt") as f:
        hiscore= f.read()
        if(hiscore !=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
            
    print(f"your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            
      
                 
    return score 

game()