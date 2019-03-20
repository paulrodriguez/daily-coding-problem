'''
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.
'''

def min_covering(intervals):
    intervals.sort(key=lambda x: x[1])

    s = set()
    s.add(intervals[0][1])

    for i in xrange(1,len(intervals)):
        if intervals[i][0] in s or intervals[i][1] in s:
            continue
        else:
            s.add(intervals[i][1])

    return s




assert min_covering([[0, 3], [2, 6], [3, 4], [6, 9]]) == set([3,6])
assert min_coverling([[0, 4], [1, 2], [5, 7], [6, 7], [6, 9], [8, 10]]) == set(2,7,9)
