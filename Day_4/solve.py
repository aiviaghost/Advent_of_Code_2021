with open("input.txt") as f:
	data = [line for line in f.read().split("\n") if line]

def win(board):
	for i in range(5):
		if all(b for b in board[i]):
			return True
		if all(b for b in (board[j][i] for j in range(5))):
			return True
	return False

numbers = [int(i) for i in data[0].split(",")]
boards = []
status = []
for i in range(1, len(data), 5):
	board = [[int(j) for j in line.split()] for line in data[i : i + 5]]
	boards.append(board)
	status.append([[False] * 5 for _ in range(5)])

def gen_ans(board, state, num):
	s = 0
	for i in range(5):
		for j in range(5):
			if not state[i][j]:
				s += board[i][j]
	print(s * num)

has_won = [False] * len(boards)
first_found = False
for num in numbers:
	for i in range(len(boards)):
		for j in range(5):
			for k in range(5):
				if boards[i][j][k] == num:
					status[i][j][k] = True
					if win(status[i]):
						has_won[i] = True
						if all(has_won):
							gen_ans(boards[i], status[i], num)
							exit(0)
						if not first_found:
							gen_ans(boards[i], status[i], num)
							first_found = True
