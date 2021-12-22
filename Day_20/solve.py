with open("input") as f:
    data = [line for line in f.read().split("\n") if line]
    algo = data[0]
    init_grid = data[1 : ]

grid = [["."] * (len(init_grid) + 200) for _ in range(100)]
for line in init_grid:
    grid.append(["."] * 100 + list(line) + ["."] * 100)
grid += [["."] * (len(init_grid) + 200) for _ in range(100)]

# 1 & 2
def solve(grid, itr):
    for _ in range(itr):
        gc = [line.copy() for line in grid]
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                num = ""
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        num += "1" if grid[i + k][j + l] == "#" else "0"
                num = int(num, 2)
                gc[i][j] = algo[num]
        grid = gc
    ans = 0
    for i in range(100 - itr, 2 * 100 + itr):
        ans += sum(_ == "#" for _ in grid[i][100 - itr : 2 * 100 + itr])
    return ans

print(solve([line.copy() for line in grid], 2))
print(solve([line.copy() for line in grid], 50))
