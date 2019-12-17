
wires = []
<<<<<<< HEAD
with open("../input/3.txt") as file:
=======
with open("../input/3-1.txt") as file:
>>>>>>> 122c99581861fd7b7fd9c631a6f04e1ebb0a84a1
    wires = file.read().strip().split("\n")


xmin=xmax=ymin=ymax = 0
for loc, wire in enumerate(wires):
    wires[loc] = wire.strip().split(",")
    xsize=ysize = 0
    for path in wires[loc]:
        amount = int(path[1:])
        if path[0] == 'U':
            xsize += amount
        elif path[0] == 'D':
            xsize -= amount
        elif path[0] == 'R':
            ysize += amount
        elif path[0] == 'L':
            ysize -= amount

        if xmin > xsize:
            xmin = xsize
        if xmax < xsize:
            xmax = xsize

        if ymin > ysize:
            ymin = ysize
        if ymax < ysize:
            ymax = ysize


grid = [[0]* (1 + ymax - ymin) for i in range (1 + xmax - xmin) ]

close = [0, 0, xmax - xmin]

intersections = []

for ind, wire in enumerate(wires):
    x = abs(xmin)
    y = abs(ymin)
    for path in wire:
        amount = int(path[1:])
        if path[0] == "U":
            for i in range(amount):
                if ind == 0:
                    grid[x+i][y] = 1
                elif grid[x+i][y] == 1:
                    dist = abs(abs(xmin) - (x+i)) + abs(abs(ymin) - y)
                    if dist > 0:
                        intersections.append([x-i, y])
                        if dist < close[2] and dist > 0:
                            close = [x+i, y, dist]
            x += amount
        elif path[0] == "D":
            for i in range(amount):
                if ind == 0:
                    grid[x-i][y] = 1
                elif grid[x-i][y] == 1:
                    dist = abs(abs(xmin) - (x-i)) + abs(abs(ymin) - y)
                    if dist > 0:
                        intersections.append([x-i, y])
                        if dist < close[2] and dist > 0:
                            close = [x-i, y, dist]
            x -= amount
        elif path[0] == "R":
            if ind == 0:
                grid[x][y:y+amount] = [1]*(amount)
            else:
                for i in range(amount):
                    if grid[x][y+i] == 1:
                        dist = abs(abs(xmin) - x) + abs(abs(ymin) - (y+i))
                        if dist > 0:
                            intersections.append([x, y+i])
                            if dist < close[2] :
                                close = [x, y+i, dist]
            y += amount
        elif path[0] == "L":
            if ind == 0:
                grid[x][y-amount:y] = [1]*(amount)
            else:
                for i in range(amount):
                    if grid[x][y-i] == 1:
                        dist = abs(abs(xmin) - x) + abs(abs(ymin) - (y-i))
                        if dist > 0:
                            intersections.append([x, y-i])
                            if dist < close[2] :
                                close = [x, y-i, dist]
            y -= amount

if __name__ == "__main__":
    print(f"Day 3 pt. 1: {close[2]}")
