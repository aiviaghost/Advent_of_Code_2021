def parse(line):
    op, coords = line.split()
    x, y, z = map(lambda b: (int(b[0]), int(b[1])), map(lambda a: a[2 : ].split(".."), coords.split(",")))
    # print(op, op == "on")
    return (op == "on", (x, y, z))

with open("input") as f:
    data = [parse(line) for line in f.readlines() if line]
# print(data)
cube = [[[False] * 101 for _ in range(101)] for _ in range(101)]

for line in data:
    op, (x, y, z) = line
    for i in range(max(x[0], -50), min(x[1], 50) + 1):
        for j in range(max(y[0], -50), min(y[1], 50) + 1):
            for k in range(max(z[0], -50), min(z[1], 50) + 1):
                # print(op, k + 50, j + 50, i + 50)
                cube[k + 50][j + 50][i + 50] = op

print(sum(sum(sum(i) for i in j) for j in cube))

