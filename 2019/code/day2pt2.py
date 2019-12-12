import day2pt1

if __name__ == "__main__":
    day2pt1.codes[1] = 0
    day2pt1.codes[2] = 0
    res = 0
    while res != 19690720:
        day2pt1.codes[1] += 1
        if day2pt1.codes[1] > 99:
            day2pt1.codes[1] = 0
            day2pt1.codes[2] += 1
        curIns = 0
        codes = [i for i in day2pt1.codes]
        while codes[curIns] == 1 or codes[curIns] == 2:
            locOne = codes[curIns+1]
            locTwo = codes[curIns+2]
            storeLoc = codes[curIns+3]

            if codes[curIns] == 1:
                codes[storeLoc] = codes[locOne] + codes[locTwo]
            else:
                codes[storeLoc] = codes[locOne] * codes[locTwo]

            curIns += 4
        res = codes[0]

    print(f"Day 2 pt. 2: {codes[1] * 100 + codes[2]}")
