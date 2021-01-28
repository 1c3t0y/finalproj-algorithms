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

def dijkstra(G, w ,s):
	d, predecesores = initialize_single_source(G, s)
	S = []
	Q = d.copy()
	Q.sort()
	while len(Q) != 0:
		u = d.index(Q[0])
		Q.pop(0)  #Simulación de la min-priority queue
		S = S + [u]
		for v in range(0, len(G[u])):
			print("")
			print(u)
			print(v)
			print(d)
				
			d, predecesores = relax(u, v, w, d, predecesores)
	return S

G = [[1, 3], [2, 3], [4], [1, 2, 4], [2, 0]]
w = [[10, 5], [1, 2], [4], [3, 9, 2.1], [6, 7]]
s = 0
print(dijkstra(G, w, s))