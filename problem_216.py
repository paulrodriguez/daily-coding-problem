'''
Given a number in Roman numeral format, convert it to decimal.
'''

def romanToNumber(s):
	if len(s) <=0:
		return 0

	roman = {
		    'M': 1000,
		    'D': 500,
		    'C': 100,
		    'L': 50,
		    'X': 10,
		    'V': 5,
		    'I': 1
		}
	n = 0

	prev = roman[s[-1]]

	n += prev#roman[prev]

	for i in range(len(s)-2,-1,-1):
		curr = roman[s[i]]

		if curr < prev:
			n -= curr
		else:
			n += curr

		prev = curr

	return n

assert romanToNumber('XIV') == 14
assert romanToNumber('MCMXCIX') == 1999
