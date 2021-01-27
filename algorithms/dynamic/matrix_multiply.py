import numpy as np

def matrix_multiply(A, B):
	A = np.array(A)
	B = np.array(B)

	if A.shape[1] != B.shape[0]:
		print("Error, incompatible dimensions")
		return None

	C = np.zeros((A.shape[0], B.shape[1]))

	for i in range(0, A.shape[0]):
		for j in range(0, B.shape[1]):
			for k in range(0, A.shape[1]):
				C[i][j] = C[i][j] + A[i][k] * B[k][j]
	
	return C.tolist()

#A = [[1,2],[3,4]]
#B = [[1,2],[3,4]]

#print(matrix_multiply(A, B))