from itertools import product

with open("input") as f:
    init_p1, init_p2 = map(lambda x: int(x) - 1, (line.split()[-1] for line in f.read().split("\n") if line))

# 1

def deterministic_die():
    side = 0
    while True:
        side = side + 1 if side < 100 else 1
        yield side

die = deterministic_die()
p1_pos, p2_pos = init_p1, init_p2
p1_score = p2_score = 0
rolls = 0
while True:
    p1_pos = (p1_pos + next(die) + next(die) + next(die)) % 10
    rolls += 3
    p1_score += p1_pos + 1
    if p1_score >= 1000:
        break

    p2_pos = (p2_pos + next(die) + next(die) + next(die)) % 10
    rolls += 3
    p2_score += p2_pos + 1
    if p2_score >= 1000:
        break

print(rolls * min(p1_score, p2_score))

# 2

from collections import defaultdict

seen = defaultdict(int)
count = 0
for p in product(range(1, 4), repeat=3):
    seen[sum(p)] += 1
print(sorted((i, j) for i, j in seen.items()))
