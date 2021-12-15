with open("input.txt") as f:
    data = [line.strip() for line in f.read().split("\n")]

split = data.index("")
dots = set(map(lambda x: tuple(map(int, x.split(","))), data[ : split]))
folds = list(map(lambda y: (y[0], int(y[1])), (x.split()[2].split("=") for x in data[split + 1 : ])))
w = max(x for x, _ in dots) + 1
h = max(y for _, y in dots) + 1
grid = [["#" if (x, y) in dots else "." for x in range(w)] for y in range(h)]

def fold_x(grid, xc):
    left, right = [row[ : xc] for row in grid], [row[xc + 1 : ] for row in grid]
    for y in range(len(right)):
        for x in range(len(right[y])):
            if right[y][x] == "#":
                left[y][-(x + 1)] = right[y][x]
    return left

def fold_y(grid, yc):
    upper, lower = [grid[i] for i in range(yc)], [grid[i] for i in range(yc + 1, len(grid))]
    for x in range(len(grid[0])):
        for y in range(len(lower)):
            if lower[y][x] == "#":
                upper[-(y + 1)][x] = lower[y][x]
    return upper

def solve(folds):
    gc = [row.copy() for row in grid]
    for dir, val in folds:
        if dir == "x":
            gc = fold_x(gc, val)
        else:
            gc = fold_y(gc, val)
    return gc

print(sum(sum(i == "#" for i in row) for row in solve(folds[:1])))
print("\n".join("".join(row) for row in solve(folds)))
