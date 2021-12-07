with open("input.txt") as f:
	data = sorted(int(i) for i in f.readline().split(","))

ans1 = ans2 =  10 ** 18
for i in range(max(data) + 1):
	less, more = list(filter(lambda x: x < i, data)), list(filter(lambda x: x > i, data))
	ans1 = min(
		sum(abs(j - i) for j in less) + sum(abs(j - i) for j in more), 
		ans1
	)
	ans2 = min(
		sum(abs(j - i) * (abs(j - i) + 1) // 2 for j in less) + sum(abs(j - i) * (abs(j - i) + 1) // 2 for j in more), 
		ans2
	)

print(ans1)
print(ans2)
