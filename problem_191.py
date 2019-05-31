'''
Given a collection of intervals,
find the minimum number of intervals 
you need to remove to make the rest of the intervals non-overlapping.
'''

def nonOverlappingIntervals(intervals):
    if len(intervals)==0:
        return 0

    intervals.sort(key=lambda x: x[1])

    prev = intervals[0]

    res = 0

    for i in range(1,len(intervals)):
        curr = intervals[i]
        if curr[1] <= prev[0] or curr[0] >= prev[1]:
            prev = curr
        else:
            res += 1

    return res


print(nonOverlappingIntervals([(7,9),(2,4),(5,8)]))
print(nonOverlappingIntervals([(0,14),(1,3),(5,7),(9,11),(13,15)]))
            
print(nonOverlappingIntervals([(0,14),(1,3),(5,7),(9,11),(13,15),(4,10)]))
print(nonOverlappingIntervals([(6,9),(3,7),(2,4),(1,3),(0,5)]))
