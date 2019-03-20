'''
Given a sorted list of integers, square the elements and give the output in sorted order.
'''
import collections
def square_sortedv1(arr):
    for i in xrange(len(arr)):
        arr[i] = arr[i]*arr[i]
    
    arr.sort()
    return arr

def square_sortedv2(arr):
    l = 0
    r = len(arr)-1
    
    c = collections.deque()
    while l <=r:
        ll = arr[l]*arr[l]
        rr = arr[r]*arr[r]

        if ll > rr:
            c.appendleft(ll)
            l += 1
        else:
            c.appendleft(rr)
            r -= 1

    return list(c)

assert square_sortedv1([-9,-2,0,2,3]) == [0,4,4,9,81]

assert square_sortedv2([-9,-2,0,2,3]) == [0,4,4,9,81]
