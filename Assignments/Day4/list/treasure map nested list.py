line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

#############################################################

column=0
coordinates=0

try:
    if position[0] =="A":
        column=1
    elif position[0] =="B":
        column=2
    elif position[0]=="C":
        column=3
    else:
        print("Enter the proper format starting with A, B, C\n")

    # Finding the List index in the map list
    coordinates= (str(position[1])+str(column))
except:
    print("ERROR format incorrect")

first_coordinate=int(coordinates[0])-1
second_coordinate=int(coordinates[1])-1
# Change in the map list
map[first_coordinate][second_coordinate]="X"


############################################
print(f"{line1}\n{line2}\n{line3}")