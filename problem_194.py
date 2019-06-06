'''
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. 
Imagine a set of n line segments connecting each point pi to qi. 
Write an algorithm to determine how many pairs of the line segments intersect.
'''


def linesIntersect(lines):
	lines.sort(key=lambda x: x[0] if x[0] > x[1] else x[1])

	print(lines)

	res = 0
	for i in range(len(lines)):
		l0 = lines[i]
		
		for j in range(i+1,len(lines)):
			l1 = lines[j]
			if min(l1[0],l1[1]) >= max(l0[0],l0[1]):
				break

			if l1[0] == l0[0] or l1[1] == l0[1]:
				continue

			if l0[0] > l0[1]:
				start = l0[1]
				end = l0[0]

				if l1[0] >= start and l1[1] <= end:
					res += 1
				elif  l

linesIntersect([(1,5),(4,3),(2,1)])
