'''
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7.
The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
'''


def nthSevenish(n):
	if n == 0:
		return False
	p = 0
	sevenish = []

	while len(sevenish) < n:
		np = 7 ** p
		tmp = [np]
		for v in sevenish:
			s = np + v
			tmp.append(s)
			if (len(sevenish) + len(tmp)) == n:
				return tmp[-1]

		sevenish += tmp

		p += 1
	return sevenish[n-1]


print(nthSevenish(1))
print(nthSevenish(2))
print(nthSevenish(3))
print(nthSevenish(4))
print(nthSevenish(5))
print(nthSevenish(6))
print(nthSevenish(7))
