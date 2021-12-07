
depths = []
cnt = 0
with open("input/day1.txt") as file:
    depths = [int(x) for x in file.read().strip().split("\n")]

if __name__ == "__main__":
    for n in range(1, len(depths)):
        if depths[n] > depths[n-1]:
            cnt += 1
    print(f"Total Increases: {cnt}")
        
