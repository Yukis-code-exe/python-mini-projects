import random

number = random.randint(1, 10)
#print(number)

while True:
    guess = input("Guess a number between 1 and 10: ")

    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number, try again")
        continue
    
    if guess < 1 or guess > 10:
        print("Number must be between 1 and 10")
        continue

    if guess != number:
        print("Wrong, try again")
    else:
        print("You guessed right!")
        break