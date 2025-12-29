import random

flashcard = [
    ("What is the index of the first item in a list? ", "0"),
    ("What data type does input() always return? ", "a string"),
    ("What keyword stops a loop immediately? ", "break")
]
counter = 0
used = [

]

card = (random.choice(flashcard))

while True:
    answer = input(card[0]).strip().lower()

    if answer != card[1]:
        print("The answer is inncorect, try again ")
        continue

    else:
        print("Correct, well done!")
        counter+=1
        print(f"{counter}/3 cards used")
    if counter >=3:
        break
        
    option = input("Would you like another question? (Y/N) ").strip().capitalize()
    used.append(card)
    newcard = (random.choice(flashcard))
    while newcard in used:
        newcard = (random.choice(flashcard))

    card = newcard

    if option == "Y":
        continue

    elif option == "N":
        break