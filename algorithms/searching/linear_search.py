def linear_search(A, v):
	for i in range(0, len(A)):
		if A[i] == v:
			return i
	return None