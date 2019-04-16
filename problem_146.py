'''
Given a binary tree where all nodes are either 0 or 1,
prune the tree so that subtrees containing all 0s are removed.
'''


'''
time complexity is O(n)
since recurse through each element only once

space complexity is O(1)
only three variables are used in each recursive call
'''
class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def prune(root):
    if root == None:
        return True
    can_prune = True if root.val==0 else False

    can_prune_left = prune(root.left)
    can_prune_right = prune(root.right)

    if can_prune_left:
        root.left = None
    else:
        can_prune = False

    if can_prune_right:
        root.right = None
    else:
        can_prune = False
    
    return can_prune

def print_tree(root):
    queue = [root]
    while len(queue) > 0:
        nq = []
        s = ""
        for n in queue:
            s += str(n.val)+" "
            if n.left != None:
                nq.append(n.left)
            if n.right != None:
                nq.append(n.right)
        print(s)
        queue = nq

root = Node(0,Node(1),Node(0,Node(1,Node(0),Node(0)),Node(0)))

prune(root)
print_tree(root)


