'''
Given the root to a binary search tree, find the second largest node in the tree.
'''

def find_largest(root):
    largest = root
    while largest != None and largest.right != None:
        largest = largest.right
    return largest

def find_second_largest(root):
    if root == None:
        return None

    if root.right == None and root.left == None:
        return None

    if root.right == None:
        return find_largest(parent.left)

    parent = root
    largest = root.right

    while largest != None and largest.right!=None:
        parent = largest
        largest = largest.right

    # this means root.right is None
    if largest.left != None:
        return find_largest(largest.left)
    else:
        return parent
