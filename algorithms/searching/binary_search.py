from math import ceil

def binary_search_r(A, x, i, j):

	m = ceil((i + j - 1) / 2)

	if x == A[m]:
		return m

	if x < A[m] and i < m:
		return binary_search_r(A, x, i, m - 1)

	elif x > A[m] and j > m:
		return binary_search_r(A, x, m + 1, j)

	else:
		return None


#arr = [ 2, 3, 4, 10, 40 ] 
#x = 10
  
# Function call 
#result = binary_search_r(arr, x, 0, len(arr)-1)
  
#if result != None: 
#   print ("Element is present at index % d" % result) 
#else: 
#    print ("Element is not present in array") 