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

x = True

while x is not False:
    RPS_list = [rock, paper, scissors]

    Player_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or 2 for Scissors: "))
    Computer_choice = random.randint(0, len(RPS_list) - 1)

    if Player_choice <= len(RPS_list) - 1:
        print(f"Player chose\n{RPS_list[Player_choice]}")
        print(f"Computer chose\n{RPS_list[Computer_choice]}")

        if Player_choice == Computer_choice:
            print(f"It is a draw")
        elif Player_choice == 0 and Computer_choice == 2:
            print(f"You won")
        elif Player_choice == 2 and Computer_choice == 0:
            print(f"You lost")
        elif Player_choice > Computer_choice:
            print(f"You won")
        elif Player_choice < Computer_choice:
            print(f"You lost")
    else:
        print(f"You lost (choice does not exist or unknown character")
    a = True
    while a is not False:
        b = input("Play again? y/N: ").lower()
        if b == "n":
            x = False
            a = False
        elif b == "y":
            a = False
        else:
            print("User input not recognised")
