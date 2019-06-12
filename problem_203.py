'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
'''


def findMin(arr):
    if len(arr) == 0:
        raise Exception('length must be greater than zero')

    s = 0
    e = len(arr)-1
    mi = arr[0]
    while s <= e:
        m = (s+e)/2
        if arr[m]>=arr[s]:
            mi = min(arr[s],mi)
            s = m + 1
        else:
            mi= min(arr[m],mi)
            e = m - 1
    return mi

print(findMin([1,2,3,4,5,6,7,8]))
print(findMin([8,1,2,3,4,5,6,7]))
print(findMin([7,8,1,2,3,4,5,6]))
print(findMin([6,7,8,1,2,3,4,5]))
print(findMin([5,6,7,8,1,2,3,4]))
print(findMin([4,5,6,7,8,1,2,3]))
print(findMin([3,4,5,6,7,8,1,2]))
print(findMin([2,3,4,5,6,7,8,1]))
print(findMin([5,7,10,3,4]))


    
