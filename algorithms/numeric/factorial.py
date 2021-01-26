def factorial_r(n):
	if n == 0:
		return 1
	return n * factorial_r(n - 1)

def factorial_i(n):
	x = 1
	for i in range(1, n + 1):
		x = i * x
	return x