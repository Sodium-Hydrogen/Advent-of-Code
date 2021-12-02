from day2pt1 import directions

position = {"x":0,"y":0,"aim":0}

if __name__ == "__main__":
    for dirc, dist in directions:
        if dirc == "forward":
            position['x'] += int(dist)
            position['y'] += int(dist)*position['aim']
        else:
            position['aim'] += int(dist)*(-1 if dirc=='up' else 1)
    print(f'The final position is {position["x"]},{position["y"]}: {position["x"]*position["y"]}')
