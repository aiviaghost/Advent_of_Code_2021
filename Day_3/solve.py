with open("input.txt") as f:
	data = [[int(i) for i in l] for l in f.read().split("\n") if l]

def bin_to_int(b):
	return int("".join(str(i) for i in b), 2)

# 1
w, h = len(data[0]), len(data)
gamma = [None for _ in range(w)]
for i in range(w):
	ones, zeros = 0, 0
	for j in range(h):
		ones += data[j][i] == 1
		zeros += data[j][i] == 0
	gamma[i] = int(ones > zeros)

gamma = bin_to_int(gamma)
epsilon = gamma ^ (2 ** gamma.bit_length() - 1)
print(gamma * epsilon)

# 2
def solve(nums, compare, i):
	if len(nums) == 1:
		return nums[0]
	gamma = None
	ones, zeros = 0, 0
	for j in range(len(nums)):
		ones += nums[j][i] == 1
		zeros += nums[j][i] == 0
	gamma = int(compare(ones, zeros))
	return solve(list(filter(lambda x: x[i] == gamma, nums)), compare, i + 1)

oxygen_rating = bin_to_int(solve(data, lambda x, y: x >= y, 0))
co2_rating = bin_to_int(solve(data, lambda x, y: x < y, 0))

print(oxygen_rating * co2_rating)
