'''
Given an array of time intervals (start, end) 
for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.
'''

def min_classrooms(intervals):
    actions = []
    for i in intervals:
        actions.append((i[0],1))
        actions.append((i[1],-1))

    actions.sort(key=lambda x: x[0])

    curr_classrooms = 0
    min_classrooms = 0
    for a in actions:
        if a[1]==1:
            curr_classrooms += 1
        else:
            min_classrooms = max(min_classrooms,curr_classrooms)
            curr_classrooms -= 1

    return min_classrooms


assert min_classrooms([(30,75),(0,50),(60,150)]) == 2
