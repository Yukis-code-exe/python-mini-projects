import random

answer = "Yellow"

while True:
    guess = input("What colour is a banna? ").strip().lower()

    if guess != "yellow":
        print("Inncorect try again ")
        input()
        continue

    else:
        print("Correct")
    break