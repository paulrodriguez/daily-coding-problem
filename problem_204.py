'''
Given a complete binary tree, count the number of nodes in faster than O(n) time
'''

def countNodes(root):
    leaves,max_depth = dfs(root,0,0,leaves)

def dfs(root,curr_depth,max_depth,leaves):

    if root.left != None:
        leaves,max_depth = dfs(root.left,curr_depth+1,max(curr_depth+1,max_depth),leaves)
    else:

        return (leaves+1,max_depth)

    if root.right != None:
        leaves,max_depth = dfs(root.right,curr_depth+1,max(curr_depth+1,max_depth),leaves)
    else:
        return (leaves,max_depth)
