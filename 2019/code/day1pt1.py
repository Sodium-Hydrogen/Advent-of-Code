

fuel = []
with open("../input/1-1.txt") as file:
    fuel.extend(file.read().strip().split("\n"))



if __name__ == "__main__":
    total = 0
    for amount in fuel:
        total += int(int(amount)/3) - 2
    print(f"Day 1 pt. 1: {total}")
