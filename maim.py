import random
from unittest.result import failfast
#snack water gun or rock paper scissors
def gamewin(comp,you):
    #if two value are equal than tie
    if comp==you:
        return None    #tie
        # all posibility when computer choose s
    elif comp =='s':
        if you=='w':
            return False  #you lose the game
        elif you=='g':
            return True    # you win
        # all posibility when computer choose w        
    elif comp =='w':
        if you=='g':
            return False
    elif you=='s': 
        return True  
    # all posibility when computer choose g         
    elif comp =='g':
        if you=='s':
            return False
    elif you=='w': 
        return True
print("computer turn: snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3) #we choose the 1,2,3 no as a random value
print(randNo)
if randNo==1:
    comp ='s'
elif randNo==2:
    comp='w'   
elif randNo==3:
    comp='g'
you=input("your turn: snake(s) water(w) or gun(g)? =")

print(f"computer choose {comp}") # f string se you can choose variable
print(f"you choose {you}")



a=gamewin(comp,you)
if a == None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose!")
            




