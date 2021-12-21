with open("input") as f:
	data = f.readline()[len("target area: ") : ].split(", ")
	x_min, x_max = map(int, data[0][2 : ].split(".."))
	y_min, y_max = map(int, data[1][2 : ].split(".."))

INF = 1e20

def simulate(vx, vy):
	valid = False
	max_y_reached = 0
	cx, cy = 0, 0
	while cx <= x_max and cy >= y_min:
		if x_min <= cx <= x_max and y_min <= cy <= y_max:
			valid = True
			break
		cx += vx
		cy += vy
		max_y_reached = max(cy, max_y_reached)
		vx = max(vx -1, 0)
		vy -= 1
	return max_y_reached if valid else -INF

ans1 = -INF
ans2 = 0
for vy in range(y_min, 2 * 10**3):
	for vx in range(1, 2 * 10**2):
		test = simulate(vx, vy)
		ans1 = max(test, ans1)
		ans2 += test != -INF

print(ans1)
print(ans2)
