test = {}

while True:
    word = input("Word here (or 'q' to quit): ").strip()

    if word == "q":
        break

    if word in test:
        test[word] += 1
    else:
        test[word] = 1

    print(test)
