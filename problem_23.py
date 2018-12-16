'''
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. 
You can move up, left, down, and right. You cannot move through walls. 
You cannot wrap around the edges of the board.
'''
# use breath first search. space complexity will be M*N
# time complexity is O(N +M)
def min_steps(matrix,start,end):
    if len(matrix) == 0:
        return None

    if len(matrix[0]) == 0:
        return None

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False]*cols for _ in xrange(rows)]
    visited[start[0]][start[1]] = True
    queue = [start]
    di = [(0,1),(0,-1),(1,0),(-1,0)]
    dist = 0
    while len(queue) > 0:
        nq = []
        for x,y in queue:
            if x == end[0] and y==end[1]:
                return dist
            for i,j in di:
                if isValidPoint(x+i,y+j,rows,cols) and visited[x+i][y+j]==False and matrix[x+i][y+j]==False:
                    visited[x+i][y+j] = True
                    nq.append((x+i,y+j))
        queue = nq
        dist += 1
                    

    return None

def isValidPoint(x,y,rows,cols):
    if x >=0 and x < rows and y>=0 and y < cols:
        return True
    return False

matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]

assert min_steps(matrix,(3,0),(0,0)) == 7
