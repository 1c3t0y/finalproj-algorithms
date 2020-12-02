from math import ceil

def binary_search_r(A, x, i, j):

	m = ceil((i + j - 1) / 2)

	if x == A[m]:
		return m

	if x < A[m] and i < m:
		binary_search_r(A, x, i, m-1)

	elif x > A[m] and j > m:
		binary_search_r(A, x, m+1, j-1)

	else:
		return None
