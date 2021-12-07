
moves = []
boards = []
with open("input/day4.txt") as file:
	moves = [int(nmb) for nmb in file.readline().strip().split(",")]
	# boards_txt = [row.strip().split(" ") for row in [board for board in file.read().replace("  ", " ").strip().split("\n\n")]]
	for board in [board.strip().splitlines() for board in file.read().replace("  ", " ").strip().split("\n\n")]:
		boards.append([[[int(ch),0] for ch in row.strip().split(" ")] for row in board])

def check(board):
	for dir in range(2):
		for y in range(5):
			cnt = 0
			for x in range(5):
				cnt += board[y][x][1] if dir else board[x][y][1]
			if cnt == 5:
				return True 
	return False

def mark_value(val):
	for b in range(len(boards)):
		for y in range(5):
			for x in range(5):
				boards[b][y][x][1] = int(boards[b][y][x][1] or boards[b][y][x][0] == val)

def score(board):
	score = 0
	for row in board:
		for cell in row:
			if cell[1] == 0:
				score += cell[0]
	return score
		


if __name__ == "__main__":
	for move in moves:
		brk = False
		mark_value(move)
		for board in boards:
			if check(board):
				print("Score of board is: {}\nWinning Number: {}\nTotal: {}".format(score(board), move, score(board)*move))
				brk = True
				break
		if brk:
			break
	