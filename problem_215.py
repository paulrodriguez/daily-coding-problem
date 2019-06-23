'''
Given the root to a binary tree, return its bottom view.
'''
class Node:
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

def bottomView(root):
	m = {}
	dfs(root,0,m)
	d = list(m.keys())

	d.sort()

	res = []
	for k in d:
		res.append(m[k])

	return res

def dfs(root,d,m):
	if root == None:
		return

	dfs(root.left,d-1,m)
	m[d] = root.val
	dfs(root.right,d+1,m)


print(bottomView(Node(5,Node(3,Node(1,Node(0)),Node(4)),Node(7,Node(6),Node(9,Node(8))))))
print(bottomView(Node(5,Node(3,Node(1,Node(0),Node(10,Node(11,Node(12,Node(13))))),Node(4)),Node(7,Node(6),Node(9,Node(8))))))
	
