'''
Given the root of a binary tree, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself.
'''

class Node:
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

def subTreeSum(root):
	if root == None:
		return 0

	freq = {}
	rec(root,freq)

	best = 0
	res = None

	for d in freq.keys():
		if freq[d] > best:
			best = freq[d]
			res = d
	return res

def rec(root,freq):
	if root == None:
		return 0

	s_left = rec(root.left, freq)
	s_right = rec(root.right, freq)

	curr_sum = root.val + s_left + s_right
	
	if curr_sum in freq:
		freq[curr_sum] += 1
	else:
		freq[curr_sum] = 1

	return curr_sum


root = Node(5,Node(2),Node(-5))

print(subTreeSum(root))
