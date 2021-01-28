def dfs_visit(G, u, color, d, predecesor, f, time):
	time += 1
	d[u] = time
	color[u] = "GRAY"

	for v in G[u]:
		if color[v] == "WHITE":
			predecesor[v] = u
			color, d, predecesor, f, time = dfs_visit(G, v, color, d, predecesor, f,  time)
	color[u] = "BLACK"
	time += 1
	f[u] = time

	return color, d, predecesor, f, time



def dfs(G):
	color = ["WHITE" for i in range(0, len(G))]
	predecesor = [None for i in range(0, len(G))]
	d = [0 for i in range(0, len(G))]
	f = [0 for i in range(0, len(G))]
	
	time = 0

	for u in range(0, len(G)):
		if color[u] == "WHITE":
			color, d, predecesor, f, time = dfs_visit(G, u, color, d, predecesor, f, time)

	return predecesor, d, f


#G = [[1,3], [4], [4, 5], [1], [3], [5]]

#predecesor, d, f = dfs(G)

#print(predecesor)
#print(d)
#print(f)