import day3pt1

stepCount = []
totalStep = 0
for inter in day3pt1.intersections:
    for wire in day3pt1.wires:
        x = abs(day3pt1.xmin)
        y = abs(day3pt1.ymin)
        pathTotal = 0
        for path in wire:
            amount = int(path[1:])
            xprev = x
            yprev = y
            if path[0] == "U":
                x += amount
            elif path[0] == "D":
                x -= amount
            elif path[0] == "R":
                y += amount
            elif path[0] == "L":
                y -= amount

            xlow = x if x < xprev else xprev
            xhigh = x if x > xprev else xprev

            ylow = y if y < yprev else yprev
            yhigh = y if y > yprev else yprev

            if (xlow<=inter[0] and xhigh>=inter[0] and y==inter[1] )or \
                (ylow<=inter[1] and yhigh>=inter[1] and x==inter[0]):
                pathTotal += abs((inter[0]-xprev) if x != xprev else (inter[1]-yprev))
                totalStep += pathTotal
                break
            else:
                pathTotal += amount

    if totalStep > 0:
        stepCount.append(totalStep)
        totalStep = 0


stepCount.sort()
print(f"Day 3 pt. 2: {stepCount[0]}")
