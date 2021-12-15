from collections import defaultdict

with open("input.txt") as f:
    data = [line.strip() for line in f.read().split("\n") if line]

template = list(data[0])
pairs = dict(tuple(x.split(" -> ")) for x in data[1:])

def step(s):
    ns = []
    for i in range(len(s) - 1):
        ns.append(s[i])
        if "".join(s[i : i + 2]) in pairs:
            ns.append(pairs["".join(s[i : i + 2])])
    ns.append(s[-1])
    return ns

# 1
c1 = template.copy()
for _ in range(10):
    c1 = step(c1)

count = defaultdict(lambda: 0)
for i in c1:
    count[i] += 1
print(max(count.values()) - min(count.values()))

# 2
count = defaultdict(lambda: 0)
for i in template:
    count[i] += 1

pc = defaultdict(lambda: 0)
for i in range(len(template) - 1):
    pc["".join(template[i : i + 2])] += 1

for _ in range(40):
    npc = pc.copy()
    for p in pc.keys():
        if pc[p] > 0 and p in pairs:
            nk1, nk2 = p[0] + pairs[p], pairs[p] + p[1]
            npc[p] -= pc[p]
            npc[nk1] += pc[p]
            npc[nk2] += pc[p]
            count[pairs[p]] += pc[p]
    pc = npc
print(max(count.values()) - min(count.values()))
