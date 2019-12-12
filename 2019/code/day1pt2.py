import day1pt1

total = 0
for amount in day1pt1.fuel:
    neededfuel = int(int(amount)/3) - 2
    while neededfuel > 0:
        total += neededfuel
        neededfuel = int(neededfuel/3) - 2


print(f"Day 1 pt. 2: {total}")
