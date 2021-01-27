import numpy as np

def matrix_chain_order(p):
	n = len(p)
	m = np.zeros((n ,n))
	s = np.zeros((n - 1, n))

	for l in range(2, n):
		for i in range(1, n - l + 1):
			j = i + l - 1
			m[i, j] = np.inf
			for k in range(i, j):
				q = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
				if q < m[i, j]:
					m[i, j] = q
					s[i, j] = k

	return m.astype(int), s.astype(int)

def print_optimal_parens(s, i, j):
	if i == j:
		print(" A" + str(i) + " ", end = "")
	else:
		print("(", end = "")
		print_optimal_parens(s, i, s[i, j])
		print_optimal_parens(s, s[i, j] + 1, j)
		print(")", end = "")




#p = (30, 35, 15, 5, 10, 20, 25)
#n = len(p) - 1

#m, s = matrix_chain_order(p)

#print(m)
#print(s)

#print_optimal_parens(s, 1, n)


