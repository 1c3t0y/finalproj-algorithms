def bfs(G, s):	
	color = ["WHITE" for v in G]
	d = ["inf" for v in G]
	predecesor = [None for v in G]

	color[s] = "GRAY"
	d[s] = 0

	Q = []
	Q.append(s)

	while Q != []:
		u = Q.pop(len(Q) - 1)
		for v in G[u]:
			if color[v] == "WHITE":
				color[v] = "GRAY"
				d[v] = d[u] + 1
				predecesor[v] = u
				Q.append(v)
		color[u] == "BLACK"

	return d, predecesor

def print_path(predecesor, s, v):
	if v == s:
		print("Nodo " + str(s), end = "")

	elif predecesor[v] == None:
		print("No existe un camino de " + str(s) + " a " + str(v))
		return None
	
	else:
		print_path(predecesor, s, predecesor[v])
		print(" -> Nodo " + str(v), end = "")


#G = [[1, 4], [0, 5], [3, 6, 5], [6, 2], [0], [1, 2, 6], [5, 2, 3], []]
#s = 1


#d, predecesor = bfs(G, s)

#print(color)
#print(d)
#print(predecesor)

#print_path(predecesor, s, 3)