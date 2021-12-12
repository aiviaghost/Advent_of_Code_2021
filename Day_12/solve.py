with open("input.txt") as f:
	data = [line for line in f.read().split("\n") if line]

# 1
nodes = set()
adj = {}
for line in data:
	u, v = line.split("-")
	nodes = nodes.union({u, v})
	if u in adj:
		adj[u].append(v)
	else:
		adj[u] = [v]
	if v in adj:
		adj[v].append(u)
	else:
		adj[v] = [u]

paths = 0
q = [("start", set())]
while q:
	next_q = []
	for curr, vis in q:
		if curr == "end":
			paths += 1
			continue
		for next in adj[curr]:
			if not next in vis:
				new_vis = vis.copy()
				if next.upper() != next:
					new_vis.add(next)
				if next != "start":
					next_q.append((next, new_vis))
	q = next_q
print(paths)

# 2
paths = 0
q = [("start", {k : 0 for k in nodes if k.upper() != k})]
while q:
	next_q = []
	for curr, vis in q:
		if curr == "end":
			paths += 1
			continue
		for next in adj[curr]:
			new_vis = vis.copy()
			if next != "start":
				if next.upper() != next:
					if new_vis[next] == 2:
						continue
					if new_vis[next] + 1 == 1 or (new_vis[next] + 1 == 2 and not any(v == 2 for v in new_vis.values())):
						new_vis[next] += 1
						next_q.append((next, new_vis))
				else:
					next_q.append((next, new_vis))
	q = next_q
print(paths)
