"""Number guesing game objectives:"""
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
mode=input("select mode of the game (easy or hard) : ")
actual_number=random.choice(range(1,101))
print(actual_number)
def guess():
    return int(input("Guess a number between 1 and 100(inclusive): "))
def game(mode,actual_number):
    t=False
    for i in range(1,11):
        if guess()==actual_number:
            t=True
            break
        elif mode=="easy" and i==5:
            t=False
            break
        else:
            t=False
            print("guess again")
            continue
    return t
if game(mode,actual_number)==True:
    print(f"you won and the corect answer is {actual_number}")
else:
    print("you lose")
