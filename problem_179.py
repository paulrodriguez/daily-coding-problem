'''
Given the sequence of keys visited by a postorder traversal of a binary search tree,
reconstruct the tree.
'''

'''
time complexity: O(n) average, O(n^2) worst
it iterates at each recursive step to check where left and right trees end from the root
space complexity: O(n)
n-1 elements get copied at recursive call based on the length of the list
'''
class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def build(l):
    if len(l)==0:
        return None
    if len(l)==1:
        return Node(l[-1])


    root = Node(l[-1])

    i = len(l)-2
    while i >=0 and l[i] > l[-1]:
        i -= 1

    root.right = build(l[i+1:len(l)-1])
    root.left = build(l[:i+1])

    return root

def printTree(root):
    queue = [root]
    while len(queue)>0:
        nq = []
        s = ''
        for n in queue:
            if n == None:
                s += 'N '
            else:
                s += str(n.val) + ' '
                nq.append(n.left)
                nq.append(n.right)


        print(s)
        queue = nq



l = [2,4,3,8,7,5]

node = build(l)

printTree(node)
print
printTree(build([6,8,7,5]))
