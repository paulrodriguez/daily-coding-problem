'''
Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, 
where h is the height of the tree. 
Write a program to compute the in-order traversal of a binary tree using O(1) space
'''
class Node:
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

def inOrder(root):
	curr = root

	while curr != None:
		if curr.left==None:
			print(curr.val)
			curr = curr.right
		else:
			parent = curr
			curr = curr.left
			prev = curr

			while prev.right != None:
				prev = prev.right

			prev.right = parent
			parent.left = None



root = Node(1,Node(2, Node(5,Node(6),Node(7) ), Node(3,Node(4)) ),Node(8,None,Node(9,Node(10))));
inOrder(root)

root2 = Node(1,Node(2,Node(4),Node(5)),Node(3))
print('')
inOrder(root2)
