'''
A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected.

For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. 
You can choose to represent the graph as either an adjacency matrix or adjacency list.

'''

def min_connected(g):
    visited = [False]*len(g)
    parent = [-1]*len(g)
    queue = [0]

    while len(queue) > 0:
        nq = []
        for v in queue:
           for w,e in enumerate(g[v]):
                if e==0:
                    continue
                if !visited[w]:
                    visited[w] = True
                    parent[w] = v
                    nq.append(w)
                else:
                    if visited[v] != w:
                        return False
        queue = nq

    return True






