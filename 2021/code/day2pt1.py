

directions = []
position = {'x':0,'y':0}

with open("../input/day2.txt") as file:
    directions = [tuple(line.split(" ")) for line in file.read().splitlines()]

if __name__ == "__main__":
    for dirc, dist in directions:
        if dirc == 'forward':
            position['x'] += int(dist)
        else:
            position['y'] += int(dist)*(-1 if dirc=='up' else 1)
    print(f'The final position is {position["x"]},{position["y"]}: {position["x"]*position["y"]}')
