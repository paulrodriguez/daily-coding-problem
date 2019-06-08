'''
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''

def rotateByK(arr,k):
	i = len(arr) - k 
	j = len(arr) - 1

	while i < j:
		tmp = arr[i]
		arr[i] = arr[j]
		arr[j] = tmp
		i += 1
		j -= 1

	i = 0
	j = len(arr) - 1 - k

	while i < j:
		tmp = arr[i]
		arr[i] = arr[j]
		arr[j] = tmp
		i += 1
		j -= 1

	i = 0
	j = len(arr) - 1
	while i < j:
		tmp = arr[i]
		arr[i] = arr[j]
		arr[j] = tmp
		i += 1
		j -= 1


	return arr

print(rotateByK([1,2,3,4,5,6],2))
print(rotateByK([1,2,3,4,5,6],6))
