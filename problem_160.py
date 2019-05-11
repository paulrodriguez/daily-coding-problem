'''
Given a tree where each edge has a weight, compute the length of the longest path in the tree.
'''
class Edge():
    def __init__(self,a,b,w):
        self.a = a
        self.b = b
        self.w = w

class Node():
    def __init__(self,key,weight,children=[]):
        self.key = key
        self.weight = weight
        self.children = children

def longest_path(root):
    best,total = dfs1(root,0,set())

def dfs1(root,total,visited):
    curr = root
    best = total
    for c in root.children:
        if c not in visited:
            visited.add(c)
            tmp1,tmp2 = dfs1(c,total+c.val,visited)
            if tmp2 > best:
                best = tmp2
                curr = tmp1
    return (curr,best)
    
n1 = Node('a'
