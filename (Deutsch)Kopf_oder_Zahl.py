import random

Choice_var = input("Bitte wählen, kopf oder Zahl: ").lower()
Coin_var = 0
Comp_Coin_Var = " "
if Choice_var == "kopf":
    Coin_var = 1

Computer_var = random.randint(0, 1)

if Computer_var == 1:
    Comp_Coin_Var = "Kopf"
else:
    Comp_Coin_Var = "Zahl"


if Coin_var == Computer_var:
    print(f"De gewinnst: Du {Choice_var}, Computer {Choice_var}")
else:
    print(f"Spiel vobie: Du {Choice_var}, Computer {Comp_Coin_Var}")