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
list_of_choice = [rock, paper, scissors]
player_input = int(input("Rock = 1 | Paper = 2 | Scissors = 3| Make your choice "))
computer_input = random.choice(list_of_choice)

if player_input == 1 and computer_input == rock:
  print(rock)
  print("versus")
  print(rock)
  print("This game is a tie")
elif player_input == 1 and computer_input == paper:
  print(rock)
  print("versus")
  print(paper)
  print("You lose this one")
elif player_input == 1 and computer_input == scissors:
  print(rock)
  print("versus")
  print(scissors)
  print("You win this one")
# ------------------------------------------------`------
elif player_input == 2 and computer_input == rock:
  print(paper)
  print("versus")
  print(rock)
  print("You win this one")
elif player_input == 2 and computer_input == paper:
  print(paper)
  print("versus")
  print(paper)
  print("This one is a tie")
elif player_input == 2 and computer_input == scissors:
  print(paper)
  print("versus")
  print(scissors)
  print("You lose this one")
#  ------------------------------------------------------ 
elif player_input == 3 and computer_input == rock:
  print(scissors)
  print("versus")
  print(rock)
  print("You lose this one")
elif player_input == 3 and computer_input == paper:
  print(scissors)
  print("versus")
  print(paper)
  print("You win this one")
elif player_input == 3 and computer_input == scissors:
  print(scissors)
  print("versus")
  print(scissors)
  print("This one is a tie")
elif player_input > 3 or player_input < 0:
    print("You didn't pick anything you lose!")
  