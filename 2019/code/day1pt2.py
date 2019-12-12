
fuel = []
with open("../input/1-1.txt") as file:
    fuel.extend(file.read().strip().split("\n"))


total = 0
for amount in fuel:
    neededfuel = int(int(amount)/3) - 2
    while neededfuel > 0:
        total += neededfuel
        neededfuel = int(neededfuel/3) - 2

    
print(f"Day 1 pt. 2: {total}")
