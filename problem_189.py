'''
Given an array of elements, return the length of the longest subarray where all its elements are distinct.
'''

'''
time complexity: O(n)
space complexity: O(n)
'''
def longestDistinctSubarray(arr):
	start = 0
	found = {}
	best = 0

	for i in range(len(arr)):
		n = arr[i]
		if n in found and found[n] >=start and found[n] <= i:
			start = found[n] + 1

		found[n] = i

		best = max(best,i - start + 1)

	return best


print(longestDistinctSubarray([5, 1, 3, 5, 2, 3, 4, 1]))

print(longestDistinctSubarray([1,2,1,1,3,4,1,7]))
