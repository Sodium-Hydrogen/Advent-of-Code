

from day4pt1 import *


for move in moves:
		mark_value(move)
		brds = boards[::]
		for i in range(len(boards)):
			if check(boards[i]):
				brds[i] = None
				if len(list(filter(None, brds))) == 0:
					print("Score of board is: {}\nWinning Number: {}\nTotal: {}".format(score(boards[i]), move, score(boards[i])*move))
		boards = list(filter(None, brds))