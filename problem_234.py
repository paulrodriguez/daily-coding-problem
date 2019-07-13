'''
Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight.
Given an undirected graph with weighted edges, compute the maximum weight spanning tree.
'''

class Graph():
	def __init__(self,V):
		self.V = V
		self.graph = []


'''
Time Complexity: O(n^2)
Space Complexity: O(n)
'''
def maxST(g):
	key = [float('-inf')]*g.V

	mstSet = [False]*g.V

	parent = [None]*g.V

	key[0] = 0
	parent[0] = -1

	for i in range(g.V):
		u = maxKey(key,mstSet)
		mstSet[u] = True
		for v in range(len(g.graph[u])):
			w = g.graph[u][v]
			if w > 0 and w > key[v] and mstSet[v] == False:
				parent[v] = u
				key[v] = w

	weight = 0
	for i in range(1,g.V):
		weight += g.graph[i][parent[i]]

	return weight
				


def maxKey(key,mstSet):
	m = float('-inf')
	res = None
	for i in range(len(key)):
		if key[i] > m and mstSet[i] == False:
			m = key[i]
			res = i

	return res





g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]]

assert maxST(g) == 30

g = Graph(9)

g.graph = [
	[0,4,0,0,0,0,0,8,0],
	[4,0,8,0,0,0,0,11,0],
	[0,8,0,7,0,4,0,0,2],
	[0,0,7,0,9,14,0,0,0],
	[0,0,0,9,0,10,0,0,0],
	[0,0,4,14,10,0,2,0,0],
	[0,0,0,0,0,2,0,1,6],
	[8,11,0,0,0,0,1,0,7],
	[0,0,2,0,0,0,6,7,0]
]
assert maxST(g) == 71
