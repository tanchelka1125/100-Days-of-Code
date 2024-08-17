print("Welcome to Treasure Island.")
print('''
        |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
''')
user_input = input("You are at a cross road. Where do you want to go?\n Type left or right").lower()
if user_input == "left":
    user_input = input("You entered a beautiful, ornate room with a pool in the middle. "
                       "Do you want to swim or wait?").lower()
    if user_input == "wait":
        user_input = input("Which door would you like to open?").lower()
        if user_input == "red" or user_input == "blue":
            print("You got attacked by an angry mob! Game Over.")
        elif user_input == "yellow":
            print("You Win!")
    elif user_input == "swim":
        print("You got eaten by an alligator! Game Over!")
elif user_input == "right":
    print("You fell into a trap! Game Over.")
