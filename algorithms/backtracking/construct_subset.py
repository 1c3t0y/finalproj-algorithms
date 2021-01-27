import numpy as np

def construct_subset(X, T):
	n = len(X)


	if T == 0:
		return []

	if T < 0 or n == 0:
		return None

	Y = construct_subset(X[0 : n - 1], T)
	if Y != None:
		return Y

	Y = construct_subset(X[0 : n - 1], T - X[n - 1])
	if Y != None:
		return Y + [X[n - 1]]

	return None


#X = [9,6,7,5,3,10,9]
#print(construct_subset(X, 15))