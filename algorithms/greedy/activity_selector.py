def activity_selector_r(s, f, k, n):
	m = k + 1

	while m <= n and s[m] < f[k]:
		m = m + 1
	
	if m <= n:
		return ["A" + str(m)] + activity_selector_r(s, f, m, n)
	
	else:
		return []


def activity_selector_i(s, f):
	n = len(s)
	A = ["A1"]
	k = 1
	for m in range(2, n):
		if s[m] >= f[k]:
			A = A + ["A" + str(m)]
			k = m
	return A

#s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
#n = 11

#print(activity_selector_r(s, f, 0, n))
#print(activity_selector_i(s, f))