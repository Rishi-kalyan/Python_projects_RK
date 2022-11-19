from Data import *
from random import *
print("hello")
def generate():
    return choice(data)
def details(account):
    name=account["Name"]
    return name
def check(guess,acc_a,acc_b):
    fa=acc_a["follower_count"]
    fb=acc_b["follower_count"]
    if(fa>fb):
        return (guess=="a")
    else:
        return (guess=="b")
def game():
    g=True
    score=0
    acc_a=generate()
    acc_b=generate()
    while g:
        acc_a=acc_b
        acc_b=generate()
        while acc_a==acc_b:
            acc_b=generate()
        print(f"A: {details(acc_a)}")
        print("Vs")
        print(f"B: {details(acc_b)}")
        guess=input("Enter A or B: ").lower()
        ans=check(guess,acc_a,acc_b)
        if(ans==True):
            score+=1
            print(f"Score: {score}")
        else:
            print(f"your score: {score}")
            g=False
game()