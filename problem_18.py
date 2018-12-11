'''
Given an array of integers and a number k, 
where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.
'''
import heapq
# brute-force approach
def max_values_subarrayv1(arr,k):
    max_vals = []
    for i in xrange(len(arr)-k+1):
        max_vals.append(max(arr[i:i+k]))
    return max_vals

# using heap
def max_values_subarrayv2(arr,k):
    if len(arr) <= k:
        return [max(arr)]

    heap = []
    res = []    
    for i in xrange(k):
        heapq.heappush(heap,-arr[k])


assert max_values_subarrayv1([10,5,2,7,8,7],3) == [10,7,8,8]
assert max_values_subarrayv1([8, 5, 10, 7, 9, 4, 15, 12, 90, 13],4) == [10,10,10,15,15,90,90]

