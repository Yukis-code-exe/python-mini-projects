import random

flashcard = [
    ("What is the index of the first item in a list? ", "0"),
    ("What data type does input() always return? ", "a string"),
    ("What keyword stops a loop immediately? ", "break"),
    ("What keyword is used for a conditional statement? ", "if"),
    ("What keyword starts a function? ", "def"),
    ("What keyword checks another condition after if? ", "elif"),
    ("What data type uses square brackets? ", "list"),
    ("What method adds an item to the end of a list? ", "append"),
    ("What keyword skips the current loop iteration? ", "continue")

]
counter = 0
used = []

card = (random.choice(flashcard))

while True:
    answer = input(card[0]).strip().lower()

    if answer != card[1]:
        print("The answer is inncorect, try again ")
        continue

    else:
        print("Correct, well done!")
        counter+=1
        print(f"{counter}/9 cards used")
    if counter >=9:
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