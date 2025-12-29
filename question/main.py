import random

quest = [
    ["What is one plus one? ", "2"],
    ["What is two plus two? ", "4"],
    ["What is one plus three? ", "4"],
]

card = (random.choice(quest))

while True:
    answer = input(card[0]).strip().lower()

    if answer != card[1]:
        print("incorrect, try again")
        continue
    else:
        print("correct!")
        break

