from math import floor

def merge(A, p, q, r):
	inf = 1000 * max(A)

	n1 = q - p + 1
	n2 = r - q
	L = []
	R = []


	for i in range(0, n1):
		L.append(A[p + i])

	for j in range(0, n2):
		R.append(A[q + j + 1])

	

	L.append(inf)
	R.append(inf)

	i = 0
	j = 0

	for k in range(p,r + 1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1

		else:
			A[k] = R[j]
			j += 1

def merge_sort(A, p, r):
	if p < r:
		q = floor((p + r) / 2)
		merge_sort(A, p, q)
		merge_sort(A, q + 1, r)
		merge(A, p ,q, r)

	return A  