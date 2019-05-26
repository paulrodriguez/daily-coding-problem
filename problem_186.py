'''
Given an array of positive integers, 
divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
'''
'''
time complexity: O(nlogn)
amount of time spent sorting. we iterate the array once

space complexity: O(1)
only four variables that are not the answers are used

'''
def divideArray(A):
	s1 = []
	s2 = []

	s1_sum = 0
	s2_sum = 0

	for i in range(len(A)-1,-1,-1):
		tmp_s1_sum = A[i] + s1_sum
		tmp_s2_sum = A[i] + s2_sum

		if abs(tmp_s1_sum - s2_sum) < abs(tmp_s2_sum - s1_sum):
			s1_sum += A[i]
			s1.append(A[i])
		else:
			s2_sum += A[i]
			s2.append(A[i])

	return (s1,s2)


print(divideArray([5,10,15,20,25]))
print(divideArray([10,100,300]))
print(divideArray([1,2,3,4,5,6,7,8,9]))
print(divideArray([1,10,100,300,900]))
print(divideArray([3,1,4,2,2,1]))
print(divideArray([40,80,100]))
	
