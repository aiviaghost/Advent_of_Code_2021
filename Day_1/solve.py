with open("input.txt") as f:
    data = [int(line) for line in f.read().split("\n") if line]

# 1
print(sum(data[i] > data[i - 1] for i in range(1, len(data))))

# 2
print(sum(sum(data[i : i + 3]) > sum(data[i - 1 : i + 2]) for i in range(1, len(data))))
