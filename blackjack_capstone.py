import random
def dealcard():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

user=[]
computer=[]

user.append(dealcard())
user.append(dealcard())
computer.append(dealcard())
computer.append(dealcard())

def calculatescore(x):
  k=sum(x)
  if(11 in x) and (k>21):
    x.remove(11)
    x.append(1)
    return(sum(x))
  else:
    return k
      
def printvalues():
  j=computer.copy()
  for i in range(1,len(j)):
    j[i]="x"
  print(f"User cards are {user}, score is: {calculatescore(user)}")
  print(f"Computer cards are {j}")
printvalues()

def blackjack():
  if(calculatescore(user)==21 and calculatescore(computer)<21):
    return f"User wins\n Computer loses, with cards {computer} and score {calculatescore(computer)}"
  elif(calculatescore(computer)==21 and (calculatescore(user)==21 or calculatescore(user)<21)):
    return f"Computer wins, with cards {computer} and score {calculatescore(computer)}"
  elif(calculatescore(user)>21):
    return f"Computer wins, with cards {computer} and score {calculatescore(computer)}"
  elif(calculatescore(computer)>21):
    return f"User wins\n Computer loses, with cards {computer} and score {calculatescore(computer)}"
  else:
    return None
def capstone():
  if(blackjack()!=None):
    print(blackjack())
  else:
    c=input("hit or stand: ")
    if(c=="hit"):
      if(calculatescore(user)>calculatescore(computer)):
        print(f"User wins\n Computer loses, with cards {computer} and score {calculatescore(computer)}")
      elif(calculatescore(user)<calculatescore(computer)):
        print(f"Computer wins, with cards {computer} and score {calculatescore(computer)}")
      elif(calculatescore(user)==calculatescore(computer)):
        print("Draw")
    elif(c=="stand"):
      if(calculatescore(computer)<16):
        computer.append(dealcard())
      user.append(dealcard())
      printvalues()
      capstone()
capstone()
