from itertools import permutations

with open("input.txt", encoding="ascii") as f:
    data = [line.strip() for line in f.readlines() if line]

# 1
ans1 = 0
for line in data:
    patterns, digits = line.split(" | ")
    for d in digits.split():
        ans1 += (len(d) == 2) or (len(d) == 3) or (len(d) == 4) or (len(d) == 7)
print(ans1)

# 2

digit_patterns = {
    "012456" : "0", 
    "25" : "1", 
    "02346" : "2", 
    "02356" : "3", 
    "1235" : "4", 
    "01356" : "5", 
    "013456" : "6", 
    "025" : "7", 
    "0123456" : "8", 
    "01235" : "9"
}
print(digit_patterns)
def solve(patterns, digits):
    correct = None
    for perm in permutations(map(str, range(7))):
        mapping = {k : v for k, v in zip("abcdefg", perm)}
        if mapping["".join(sorted(mapping[c] for c in "acedgfb"))] == "8":
            print(mapping)
        found_digits = 0
        for pattern in patterns:
            possible_digit = "".join(sorted(mapping[c] for c in pattern))
            if possible_digit in digit_patterns:
                found_digits += 1
        if found_digits == 10:
            correct = mapping
            break
    return int("".join(digit_patterns["".join(sorted(correct[c] for c in pattern))] for pattern in digits))


ans2 = 0
for line in data:
    patterns, digits = line.split(" | ")
    ans2 += solve(patterns.split(), digits.split())
print(ans2)
