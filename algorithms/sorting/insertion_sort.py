def insertion_sort_increasing(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = key
	return A

def insertion_sort_decreasing(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0 and A[i] < key):
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = key
	return A

#A = [5, 2, 4, 6, 1, 3]

#print(insertion_sort_decreasing(A))
