import random
names_string = input("Gib mir alle Namen, durch Komma getrennt. ")
names = names_string.split(",")

list_size = len(names)
var_random = random.randint(0, list_size - 1)

print(f"{names[var_random]} wird das Essen heute kaufen!!")