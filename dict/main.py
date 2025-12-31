#test = {"hours played": "069", 
#        "games played": "2",
#        "friends online": "5"
#        }

#test["games played" += 1]

#for "friends online" in test:
##    print(test["friends online"])
#else:
#    print("2222")

#Start with an empty dictionary

#Ask the user to type a word

#Apply the “exists → update / not exists → create” logic

#Print the dictionary after each input

test = {}



while True:
    word = input("Enter word here or (q) to quit ")
    if word == "q":
        break

    if word in test:
        test[word] += 1
    
    else:
        test[word] = 1

    print(test)