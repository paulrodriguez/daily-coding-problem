'''
Let X be a set of n intervals on the real line. 
We say that a set of points P "stabs" X if every interval in X contains at least one point in P.
 Compute the smallest set of points that stabs X.
'''

def minPointSet(intervals):
	if len(intervals) == 0:
		return []

	intervals.sort(key=lambda x: x[1])

	prev = intervals[0]

	start = prev[1]
	end = prev[1]

	for i in range(1,len(intervals)):
		curr = intervals[i]

		if prev[1] < curr[0]:
			end = curr[0]
		elif end < curr[0]:
			end = curr[0]
		prev = curr

	return (start,end)


print(minPointSet([(0,17),(4,9),(8,15),(14,19)]))
print(minPointSet([(21,25),(0,17),(4,9),(8,15),(14,19)]))
print(minPointSet([(1,4),(4,5),(7,9),(9,12)]))
print(minPointSet([(0,9),(1,10),(4,11),(2,5)]))
