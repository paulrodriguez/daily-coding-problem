'''
A unival tree (which stands for "universal value") 
is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
'''
class Node:
    def __init__(self,v,left=None,right=None):
        self.v = v
        self.left = left
        self.right = right

def count_unival_helper(root):
    if root == None:
        return (0,True)

    lc, lu = count_unival_helper(root.left)
    rc, ru = count_unival_helper(root.right)

    is_unival = False
    total_unival = lc + rc
    if lu == True and ru == True:
        if (root.left == None or root.left.v==root.v) and (root.right==None or root.right.v==root.v):
            is_unival = True
            total_unival += 1

    return (total_unival,is_unival)

def count_unival(root):
    cnt, tmp = count_unival_helper(root)
    return cnt

root = Node(0,Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))

assert count_unival(root) == 5


