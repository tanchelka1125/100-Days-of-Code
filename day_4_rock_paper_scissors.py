import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_input == 0:
    user_input = rock
    print(rock)
elif user_input == 1:
    user_input = paper
    print(paper)
elif user_input == 2:
    user_input = scissors
    print(scissors)
else:
    print("You've entered a wrong input")

computer_input = random.randint(0, 2)

if computer_input == 0:
    computer_input = rock
    print(rock)
elif computer_input == 1:
    computer_input = paper
    print(paper)
elif computer_input == 2:
    computer_input = scissors
    print(scissors)

if user_input == computer_input:
    print("It's a draw")
elif user_input == rock and computer_input == scissors:
    print("You won this round.")
elif user_input == rock and computer_input == paper:
    print("You lost this round.")
elif user_input == scissors and computer_input == rock:
    print("You lost this round.")
elif user_input == scissors and computer_input == paper:
    print("You won this round.")
elif user_input == paper and computer_input == rock:
    print("You won this round.")
elif user_input == paper and computer_input == scissors:
    print("You lost this round.")