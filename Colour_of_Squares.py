#receiving grid square from user
grid_position = input("Enter a chess board square: ")

#finding column and row from input
column = grid_position[0]
row = grid_position[1]

#converting column to lowercase
column = column.lower()

#converting row to int
row = int(row)

#finding if row starts with black square or white square
if column == "a" or column == "c" or column == "e" or column == "g":
    first_block = "Black"
else: 
    first_block = "White"

#rows starting with black
if first_block == "Black":
    if row % 2 == 0:
        final_block = "white"
    else:
        final_block = "black"

#rows starting with white
if first_block == "White":
    if row % 2 == 0:
        final_block = "black"
    else: 
        final_block = "white"

#printing result to user (concatenation):
print("That square is " + final_block + ".")