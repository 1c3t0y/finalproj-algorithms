def fibonacci_r(n):
	
	if n == 0:
		return 0
	
	if n == 1:
		return 1

	x = fibonacci_r(n - 1)
	y = fibonacci_r(n - 2)

	return x + y

def fibonacci_i(n):

	if n == 0:
		return 0

	x = 0
	y = 1

	for i in range(1, n):
		z = x + y
		x = y
		y = z

	return y

#print(fibonacci_i(10))