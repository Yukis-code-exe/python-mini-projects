# user input call inventory display it clean
# add % drops rates
# pity system
# save inventory to file per name.

import random

loot = ["common", "rare", "ultra rare", "legendary", "forsaken"]

inventory = {}

count = 0

answer = input("Do you want to open a box? (Y/N) ").strip().title()
if answer != "Y":
    exit()
else:
    while True:
        gain = random.choice(loot)
        count += 1
        print("You got ", gain)
        print("You have opened ", count, "boxes. ")

        if gain in inventory:
            inventory[gain] += 1
        else:
            inventory[gain] = 1
        print(inventory)
        option = input("Do you want to open another? (Y/N) ").strip().title()
        if option == "Y":
            continue
        elif option == "N":
            break

    
    

