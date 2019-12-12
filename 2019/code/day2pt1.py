
codes = []
with open("../input/2-1.txt") as file:
    codes.extend(file.read().strip().split(","))

codes = [int(i) for i in codes]


if __name__ == "__main__":
    codes[1] = 12
    codes[2] = 2
    curIns = 0
    while codes[curIns] == 1 or codes[curIns] == 2:
        locOne = codes[curIns+1]
        locTwo = codes[curIns+2]
        storeLoc = codes[curIns+3]

        if codes[curIns] == 1:
            codes[storeLoc] = codes[locOne] + codes[locTwo]
        else:
            codes[storeLoc] = codes[locOne] * codes[locTwo]

        curIns += 4

    print(f"Day 2 pt. 1: {codes[0]}")
