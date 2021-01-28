def initialize_single_source(G, s):
	d = [9999999 for v in G]
	predecesores = [None for v in G]
	d[s] = 0
	return d, predecesores

def relax(u, v, w, d, predecesores):
	if d[v] > d[u] + w[u][v]:
		d[v] = d[u] + w[u][v]
		predecesores[v] = u
	return d, predecesores

def bellman_ford(G, w, s):
	d, predecesores = initialize_single_source(G, s)

	for u in range(0, len(G)) :
		for v in range(0, len(G[u])):
			print("")
			print(w[u][v])
			d, predecesores = relax(u, v, w, d, predecesores)

	for u in range(0, len(G)) :
		for v in range(0, len(G[u])):
			if d[v] > d[u] + w[u][v]:
				return False
	return True


#G = [[1, 3], [2, 3, 4], [], [2, 4], [2]]
#w = [[6, 7], [5, 8, 4], [], [3, 9], [7]]
#s = 0
#print(bellman_ford(G, w, s))

