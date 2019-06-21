'''
Given a column number, return its alphabetical column id.
'''

def getColumnId(col_num):
	s = ''
	while col_num > 0:
		rem = col_num % 26
		col_num = col_num // 26
		s = chr(rem+96)+s
	return s.upper()


assert getColumnId(1) == "A"
assert getColumnId(27) == "AA"
assert getColumnId(28) == "AB"
assert getColumnId(29) == "AC"
assert getColumnId(30) == "AD"
