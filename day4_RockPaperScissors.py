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
import random

games_img = []

USER = int(input("Rock, Paper or Scissors where 0 for Rock, 1 for Paper and 2 for Scissors?: "))
COMPUTER = random.randint(0, 2)

if USER == 0 and COMPUTER == 2: 
    print(f"Computer chose {COMPUTER}, you win!")
elif COMPUTER > USER:
    print("You lose")
elif USER == COMPUTER:
    print("Its a draw")
elif COMPUTER == 0 and USER == 2:
    print("You lose")
elif USER > COMPUTER:
    print("You win")
elif USER >= 3 or USER < 0:
    print("YOu typed an invalid number, you lose!")
print(USER)

