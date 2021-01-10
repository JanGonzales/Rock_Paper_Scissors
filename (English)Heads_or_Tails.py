import random

Choice_var = input("Please choose, Heads or Tails: ").lower()
Coin_var = 0
Comp_Coin_Var = " "
if Choice_var == "heads":
    Coin_var = 1

Computer_var = random.randint(0, 1)

if Computer_var == 1:
    Comp_Coin_Var = "heads"
else:
    Comp_Coin_Var = "tails"


if Coin_var == Computer_var:
    print(f"You win: You {Choice_var}, Computer {Choice_var}")
else:
    print(f"Game Over: You {Choice_var}, Computer {Comp_Coin_Var}")