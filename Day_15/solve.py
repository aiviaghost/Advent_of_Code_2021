from heapq import heappush as push, heappop as pop
from collections import defaultdict

with open("input.txt") as f:
    grid = [[int(i) for i in line] for line in f.read().split("\n") if line]

def dijkstra(grid):
    w, h = len(grid[0]), len(grid)
    dist = defaultdict(lambda: 1e18)
    dist[(0, 0)] = 0
    vis = set()
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(0, (0, 0))]
    while q:
        _, curr = pop(q)
        if curr in vis:
            continue
        vis.add(curr)
        for x, y in neighbours:
            nx, ny = curr[0] + x, curr[1] + y
            if 0 <= nx < w and 0 <= ny < h:
                new_dist = dist[curr] + grid[ny][nx]
                if new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist
                    push(q, (new_dist, (nx, ny)))
    return dist[(w - 1, h - 1)]

print(dijkstra(grid))

w, h = len(grid[0]), len(grid)
big_grid = [[0] * w * 5 for _ in range(h * 5)]
for i in range(h):
    for j in range(w):
        big_grid[i][j] = grid[i][j]
for i in range(h * 5):
    for j in range(w * 5):
        if i >= h and j < w:
            big_grid[i][j] = big_grid[i - h][j] + 1 if big_grid[i - h][j] < 9 else 1
        elif i < h and j >= w:
            big_grid[i][j] = big_grid[i][j - w] + 1 if big_grid[i][j - w] < 9 else 1
        elif i >= h and j >= w:
            big_grid[i][j] = big_grid[i - h][j] + 1 if big_grid[i - h][j] < 9 else 1

print(dijkstra(big_grid))
