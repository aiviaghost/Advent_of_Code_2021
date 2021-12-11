from math import prod

with open("input.txt") as f:
    data = [[int(i) for i in line] for line in f.read().split("\n") if line]

# 1
ans = 0
neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
lowpoints = []
w, h = len(data[0]), len(data)
for i in range(h):
    for j in range(w):
        include = True
        for nx, ny in neighbours:
            if 0 <= j + nx < w and 0 <= i + ny < h:
                include = include and data[i + ny][j + nx] > data[i][j]
        ans += include * (data[i][j] + 1)
        if include:
            lowpoints.append((j, i))
print(ans)

# 2
areas = []
vis = [[False] * w for _ in range(h)]
for sx, sy in lowpoints:
    if vis[sy][sx]:
        continue
    vis[sy][sx] = True
    area = 1
    q = [(sx, sy)]
    while q:
        next_q = []
        for cx, cy in q:
            for x, y in neighbours:
                nx = cx + x
                ny = cy + y
                if 0 <= nx < w and 0 <= ny < h and data[ny][nx] != 9 and not vis[ny][nx]:
                    vis[ny][nx] = True
                    area += 1
                    next_q.append((nx, ny))
        q = next_q
    areas.append(area)
print(prod(sorted(areas)[-3:]))
