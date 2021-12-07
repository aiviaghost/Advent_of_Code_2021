with open("input.txt") as f:
	fishes = [int(i) for i in f.readline().split(",")]

# 1
for _ in range(80):
	next_fishes = []
	for f in fishes:
		if f == 0:
			f = 6
			next_fishes.append(8)
		else:
			f -= 1
		next_fishes.append(f)
	fishes = next_fishes

print(len(fishes))

# 2
dp = [[0] * 9 for _ in range(257)]
for i in range(9):
	dp[0][i] = 1
for i in range(1, 257):
	for j in range(9):
		if i >= j + 1:
			dp[i][j] = dp[i - j - 1][6] + dp[i - j - 1][8]
		else:
			dp[i][j] = dp[i - 1][j]

with open("input.txt") as f:
	fishes = [int(i) for i in f.readline().split(",")]

print(sum(dp[256][f] for f in fishes))
