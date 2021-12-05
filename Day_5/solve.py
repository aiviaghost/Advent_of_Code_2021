with open("input.txt") as f:
    data = [line for line in f.read().split("\n") if line]

lines = []
considerations = []
mx, Mx, my, My = 0, 0, 0, 0
for line in data:
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    Mx, My = max(x1, x2, Mx), max(y1, y2, My)
    lines.append((x1, y1, x2, y2))
    if x1 == x2 or y1 == y2:
        considerations.append((x1, y1, x2, y2))

grid = [[0] * (Mx + 1) for _ in range(My + 1)]

for line in considerations:
    x1, y1, x2, y2 = line
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][x1] += 1
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][i] += 1
# 1
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] >= 2:
            ans += 1
print(ans)

# 2
grid = [[0] * (Mx + 1) for _ in range(My + 1)]
for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][x1] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][i] += 1
    else:
        if y1 < y2:
            x = x1
            for i in range(y1, y2 + 1):
                grid[i][x] += 1
                if x1 > x2:
                    x -= 1
                else:
                    x += 1
        else:
            x = x2
            for i in range(y2, y1 + 1):
                grid[i][x] += 1
                if x2 > x1:
                    x -= 1
                else:
                    x += 1

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] >= 2:
            ans += 1
print(ans)
