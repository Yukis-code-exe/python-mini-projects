import random

number = random.randint(1, 20)

while True:
    guess = input("Guess a number between 1 and 20 ")

    try:
        guess =int(guess)
    except ValueError:
        print("That's not a number")
        continue

    if guess < 1 or guess > 20:
        print("The number must be between 1 and 20")
        continue

    if guess != number:
        print("You guess wrong!")
        continue
    
    else:
        print("You guessed right!")
        break
