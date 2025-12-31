import random

boxes = 0
results = {}

for _ in range(10_000):
    roll = random.randint(1, 100)

    if roll <= 70:
        loot = "common"

    elif roll >= 71 and roll <= 90:
        loot = "rare"

    elif roll >= 91 and roll <= 97:
        loot = "ultra rare"

    elif roll >= 98 and roll <= 99:
        loot = "legendary"

    elif roll == 100:
        loot = "forsaken"

    if loot in results:
        results[loot] += 1
    else:
        results[loot] = 1
    boxes += 1

for loot, count in results.items():
    percent = (count / 10_000) * 100
    print(f"{loot}: {percent:.2f}%")
print("You opened ", boxes, "boxes!")
print(results)

