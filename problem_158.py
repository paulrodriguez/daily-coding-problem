'''
You are given an N by M matrix of 0s and 1s.
Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.
'''

'''
space complexity: O(1)
each recursive call takes constant space

time complexity: O(n)
n is the number of elements in the matrix
'''
def ways_to_bottom(matrix):
    if len(matrix)==0:
        return 0

    l = len(matrix[0])
    if l == 0:
        return 0

    for i in range(1,len(matrix)):
        if l != len(matrix[i]):
            return 0

    
    start = (0,0)
    dst = (len(matrix)-1,len(matrix[0])-1)
    dirs = [(1,0),(0,1)]
    return rec(dirs,matrix,start,dst,0)

def rec(dirs,matrix,curr,dst,total):
    if curr[0] == dst[0] and curr[1] == dst[1]:
        if matrix[curr[0]][curr[1]]!=1:
            return total+1
        else:
            return total
    if curr[0] >= len(matrix) or curr[1]>=len(matrix[0]):
        return total

    if matrix[curr[0]][curr[1]] == 1:
        return total

    for x,y, in dirs:
        total = rec(dirs,matrix,(curr[0]+x,curr[1]+y),dst,total)

    return total





assert ways_to_bottom([[0,0,1],[0,0,1],[1,0,0]]) == 2
assert ways_to_bottom([[1,0,1],[0,0,1],[1,0,0]]) == 0
assert ways_to_bottom([[],[],[]]) == 0
assert ways_to_bottom([[0],[0],[0,1]]) == 0
assert ways_to_bottom([[0,0,0],[0,0,0],[0,0,0]]) == 6
