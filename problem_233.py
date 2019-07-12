'''
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
'''

def fib(n):
	if n == 0:
		return 0

	if n == 1 or n == 2:
		return 1

	
	curr = 0
	prev1 = 1
	prev2 = 1

	for i in range(3,n+1):
		curr = prev1+prev2

		prev1 = prev2
		prev2 = curr


	return curr


assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
