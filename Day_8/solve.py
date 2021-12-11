with open("input.txt") as f:
    data = [line.strip() for line in f.readlines() if line]

# 1
ans1 = 0
for line in data:
    patterns, digits = line.split(" | ")
    for d in digits.split():
        ans1 += (len(d) == 2) or (len(d) == 3) or (len(d) == 4) or (len(d) == 7)
print(ans1)

# 2
def solve(patterns, digits):
    pass

ans2 = 0
for line in data:
    patterns, digits = line.split(" | ")
    ans2 += solve(patterns.split(), digits.split())
print(ans2)
