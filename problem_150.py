'''
Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.
'''
import heapq
import math
def nearestPoints(points,central,k):
    heap = []
    cx,cy = central
    for x,y in points:
        d = math.sqrt((x-cx)*(x-cx) + (y-cy)*(y-cy))
        heapq.heappush(heap,(-d,x,y))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for d1,x1,y1 in heap:
        res.append((x1,y1))

    return res

l = [(0,0),(5,4),(3,1)]

print(nearestPoints(l,(1,2),2))
    
        





