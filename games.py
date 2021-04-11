# Game Guess:        

import random
comp = (random.randint(1,50))
guess = 0
player = None
while player != comp:
    player = int(input("Enter a number : "))
    guess += 1
    if player == comp:
        print("Win")
    else :
        if player > comp:
            print("you need to enter a smaller number")
        else :
            print("You need to enter a larger number") 
print(f"The number of guess is : {guess}")    

print(comp)