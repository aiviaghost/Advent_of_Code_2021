from functools import reduce

with open("input.txt") as f:
    data = [line for line in f.read().split("\n") if line]

table = {
    ")" : 3, 
    "]" : 57, 
    "}" : 1197, 
    ">" : 25137
}

opposite = {
    "}" : "{", 
    ")" : "(", 
    ">" : "<", 
    "]" : "["
}

incomplete = []
ans = 0
for line in data:
    stack = []
    is_incomplete = True
    for c in line:
        if c in "<({[":
            stack.append(c)
        else:
            if opposite[c] != stack[-1]:
                is_incomplete = False
                ans += table[c]
                break
            else:
                stack.pop()
    if len(stack) > 0 and is_incomplete:
        incomplete.append(stack)
print(ans)

# 2

table2 = {
    ")" : 1, 
    "]" : 2, 
    "}" : 3, 
    ">" : 4
}

scores = [reduce(lambda x, y: 5 * x + y, (table2[{v : k for k, v in opposite.items()}[c]] for c in reversed(stack))) for stack in incomplete]
print(sorted(scores)[len(scores) // 2])
