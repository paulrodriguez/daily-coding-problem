'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
'''

def longest1s(n):
	c = 0
	m = 0

	while n > 0:
		if (n&1)==1:
			c += 1
		else:
			m = max(m,c)
			c = 0

		n = n >> 1

	return m

assert longest1s(156) == 3
assert longest1s(85) == 1
