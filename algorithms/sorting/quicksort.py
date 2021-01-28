def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1


def quicksort(A, p, r):
	if p < r:
		q = partition(A, p ,r)
		quicksort(A, p, q - 1)
		quicksort(A, p + 1, q)
	return A


#A = [3,4,5,6,7,3,2,1,8,6]

#print(quicksort(A, 0, len(A) - 1))