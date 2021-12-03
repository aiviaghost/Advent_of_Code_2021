with open("input.txt") as f:
	data = list(map(lambda x: (x[0], int(x[1])), (line.split() for line in f.read().split("\n") if line)))

# 1
horizontal, depth = 0, 0
for op, val in data:
	if op == "forward":
		horizontal += val
	elif op == "down":
		depth += val
	elif op == "up":
		depth -= val
print(horizontal * depth)

# 2
horizontal, depth, aim = 0, 0, 0
for op, val in data:
	if op == "forward":
		horizontal += val
		depth += aim * val
	elif op == "down":
		aim += val
	elif op == "up":
		aim -= val
print(horizontal * depth)
