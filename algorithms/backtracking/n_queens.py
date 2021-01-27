def n_queens_r(Q, r):
	n = len(Q)

	if(r == n):
		print(Q)

	for j in range(0, n):
		legal = True
		for i in range(0, r):
			if(Q[i] == j or Q[i] == (j + r - i) or Q[i] == (j - r + i)):
				legal = False

		if legal:
			Q[r] = j
			n_queens_r(Q, r + 1)



#Q = [0 for i in range(0, 8)]
#print(n_queens_r(Q, 0))

# 3 6 2 7 1 4 0 5