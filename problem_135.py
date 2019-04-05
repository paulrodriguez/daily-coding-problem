'''
Given a binary tree, find a minimum path sum from root to a leaf.

'''
class Node:
    def __init__(self,val: int,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    s, res = dfs(root,0,[])
    return res

def dfs(root, s,res):
    if root == None:
        return (s,res)

    curr_sum = s + root.val
    curr_res = res + [root.val]

    # if no left and right children, this is a leaf noen
    if root.left == None and root.right==None:
        return (curr_sum,curr_res)

    min_sum = float('inf')
    min_res = []
    
    if root.left != None:
        left_sum, left_res = dfs(root.left,curr_sum,curr_res)
        if left_sum < min_sum:
            min_sum = left_sum
            min_res = left_res

    if root.right != None:
        right_sum, right_res = dfs(root.right, curr_sum,curr_res)
        if right_sum < min_sum:
            min_sum = right_sum
            min_res = right_res
            
    return (min_sum,min_res)

#create binary tree
root = Node(10,Node(5,None,Node(2)),Node(5,None,Node(1,Node(-1),None)))
root2 = Node(10,Node(-5,None,Node(2)),Node(5))
assert min_path_sum(root) == [10,5,1,-1]

assert min_path_sum(root2) == [10,-5,2]
