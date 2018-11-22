'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.
'''

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root == None:
        return '#'
    s = root.val
    s += ','+serialize(root.left)
    s += ','+serialize(root.right)
    
    return s

def deserializeUtil(nodes,pos):
    if pos>=len(nodes):
        return (pos,None)
    if nodes[pos] == '#':
        return (pos,None)

    root = Node(nodes[pos])
    pos, root.left = deserializeUtil(nodes,pos+1)
    pos, root.right = deserializeUtil(nodes,pos+1)

    return (pos,root)

def deserialize(s):
    nodes = s.split(',')
    c,root = deserializeUtil(nodes,0)
    return root

node = Node('root', Node('left', Node('left.left')), Node('right',None,Node("right.right")))

assert serialize(node) == 'root,left,left.left,#,#,#,right,#,right.right,#,#'

assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right.val == 'right'
