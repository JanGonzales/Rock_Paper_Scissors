row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Wo willst du den Schatz hinstellen? ")
row = int(position[0])
column = int(position[1])

map [column - 1] [row - 1] = " X "
print(f"{row1}\n{row2}\n{row3}")