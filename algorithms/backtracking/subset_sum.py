def subset_sum(X, T):
	n = len(X)

	if T == 0:
		return True

	elif T < 0 or  n == 0:
		return False

	else:
		return subset_sum(X[0 : n - 1], T) or subset_sum(X[0 : n - 1], T - X[n - 1])