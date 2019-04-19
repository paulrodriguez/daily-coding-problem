'''
Given a list of numbers L,
implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).
'''
'''
time complexity: O(n)
need to calculate the prefix at each index in list
for preprocessing

space complexity: O(n)
extra array is needed to store the prefix array
'''
def preprocess(arr):
    i = 1
    arr2 = [0]*len(arr)
    arr2[0] = arr[0]
    while i < len(arr):
        arr2[i] = arr[i] + arr2[i-1]
        i += 1

    return arr2

'''
time complexity: O(1)
with a preprocessed array, computations are constant

space complexity: O(1)
only result variable is needed
'''
def sum(arr,arr2,i,j):
    if i < 0 or i >=len(arr) or j < 0 or j > len(arr):
        return False

    s = 0
    if j == len(arr):
        j -= 1
        s +=arr2[j]
    s += arr[j] - arr[i] + arr2[i] - arr2[j]

    return s


arr = [1,2,3,4,5]
pre = preprocess(arr)

assert sum(pre,arr,1,3) == 5
assert sum(pre,arr,0,4) == 10
assert sum(pre,arr,0,5) == 15
