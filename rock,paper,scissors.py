import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
map= [rock,paper, scissors]
you= int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
if you>=3 or you<0:
  print("Its invalid number, You lose!")
else:
  print(map[you])
  
  computer= random.randint(0,2)
  print("Computer choose:")
  print(map[computer])
  if you ==0 and computer ==2:
    print("You win!")
  elif computer==0 and you==2:
    print("You Lose!")
  elif computer>you:
    print("You Lose")
  elif you>computer:
    print("You win!")
  elif computer == you :
    print("Its drew" )
