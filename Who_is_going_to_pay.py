import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

list_size = len(names)
var_random = random.randint(0, list_size - 1)

print(f"{names_string[var_random]} is going to buy the meal today!")