'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
'''

def smallest_missing_positive(arr):
    if len(arr) == 0:
        return 1
    if len(arr)==1:
        if arr[0] == 1:
            return 2
        else:
            return 1

    for i in xrange(len(arr)):
        if arr[i] <= 0:
            arr[i] = len(arr)*2
    
    for n in arr:
        # make sure n is a range in array and 
        v = abs(n)-1
        if v >=0 and v < len(arr) and arr[v]>0:
            arr[v] *= -1

    for i in xrange(len(arr)):
        if arr[i] > 0:
            return i+1
    return len(arr) + 1


assert smallest_missing_positive([3,4,-1,1]) == 2
assert smallest_missing_positive([1,2,0]) == 3
assert smallest_missing_positive([3,2,1]) == 4

