def lcs_length(X, Y):
	m = len(X)
	n = len(Y)

	b = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]
	c = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if X[i - 1] == Y[j - 1]:
				c[i][j] = c[i - 1][j - 1] + 1
				b[i][j] = "LUD"

			elif c[i - 1][j] >= c[i][j - 1]:
				c[i][j] = c[i - 1][j]
				b[i][j] = "UP"

			else:
				c[i][j] = c[i][j - 1]
				b[i][j] = "LEFT"

	return c, b

def print_lcs(b, X, i, j):
	if  i == 0 or j == 0:
		return
	if b[i][j] == "LUD":
		print_lcs(b, X, i - 1, j - 1)
		print(X[i - 1], end = "")

	elif b[i][j] == "UP":
		print_lcs(b, X, i - 1, j)

	else:
		print_lcs(b, X, i, j - 1)


#X = ["A", "B", "C", "B", "D", "A", "B"]
#Y = ["B", "D", "C", "A", "B", "A"]

#c, b = lcs_length(X, Y)

#print_lcs(b, X, len(X), len(Y))