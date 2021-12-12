from itertools import permutations

with open("input.txt", encoding="ascii") as f:
    data = [line.strip() for line in f.readlines() if line]

# 1
ans1 = 0
for line in data:
    patterns, digits = line.split(" | ")
    for d in digits.split():
        ans1 += (len(d) == 2) or (len(d) == 3) or (len(d) == 4) or (len(d) == 7)
print(ans1)

# 2

digit_patterns = {
    "012456" : "0", 
    "25" : "1", 
    "02346" : "2", 
    "02356" : "3", 
    "1235" : "4", 
    "01356" : "5", 
    "013456" : "6", 
    "025" : "7", 
    "0123456" : "8", 
    "012356" : "9"
}

def solve(patterns, digits):
	correct = None
	for perm in permutations(map(str, range(7))):
		mapping = {k : v for k, v in zip('abcdefg', perm)}
		if all(("".join(sorted(mapping[c] for c in digit)) in digit_patterns) for digit in patterns):
			correct = mapping
			break
	return int("".join(digit_patterns["".join(sorted(correct[c] for c in digit))] for digit in digits))

ans2 = 0
for line in data:
    patterns, digits = line.split(" | ")
    ans2 += solve(patterns.split(), digits.split())
print(ans2)
