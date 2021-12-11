with open("input.txt") as f:
    data = [[int(i) for i in line] for line in f.read().split("\n") if line]

# 1 & 2
ans1 = 0
ans2 = 0
day = 1
while not ans1 or not ans2:
    flashed = [[False] * 10 for _ in range(10)]
    q = []
    for i in range(10):
        for j in range(10):
            data[i][j] += 1
            if data[i][j] > 9:
                q.append((j, i))
    while q:
        next_q = []
        for cx, cy in q:
            if flashed[cy][cx]:
                continue
            if data[cy][cx] > 9:
                flashed[cy][cx] = True
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (x, y) != (0, 0):
                            nx = cx + x
                            ny = cy + y
                            if 0 <= nx < 10 and 0 <= ny < 10:
                                data[ny][nx] += 1
                                next_q.append((nx, ny))
        q = next_q
    sum_flashed = sum(sum(map(int, i)) for i in flashed)
    if day <= 100:
        ans1 += sum_flashed
    if sum_flashed == 100:
        ans2 = day
    for i in range(10):
        for j in range(10):
            if flashed[i][j]:
                data[i][j] = 0
    day += 1
print(ans1)
print(ans2)
