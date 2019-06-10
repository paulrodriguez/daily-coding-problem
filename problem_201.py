'''
You are given an array of arrays of integers, 
where each array corresponds to a row in a triangle of numbers.

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value 
eventually ending with an entry on the bottom row.

Write a program that returns the weight of the maximum weight path.
'''

'''
using DFS, it checks all paths
'''
def max_weight(triangle):
    if len(triangle) == 0:
        return 0
    #best = float('-inf')
    return dfs(triangle,0,0,0)

def dfs(triangle,row,pos,weight):
    if row==len(triangle):
        return weight

    curr = weight+triangle[row][pos]
    w1 = dfs(triangle,row+1,pos,curr)
    w2 = dfs(triangle,row+1,pos+1,curr)

    return max(w1,w2)

'''
time complexity: O(N) 
space complexity: O(1): updating in-place
'''
def max_weight_dp(triangle):
    if len(triangle) == 0:
        return 0

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            w = float('-inf')
            if j < len(triangle[i-1]) and j >=0:
                w = max(w,triangle[i-1][j]+triangle[i][j])

            if (j-1) < len(triangle[i-1]) and (j-1) >=0:
                w = max(w,triangle[i-1][j-1] + triangle[i][j])

            triangle[i][j] = w

    return max(triangle[-1])

print(max_weight([[1],[2,3],[1,5,1]]))
print(max_weight_dp([[1],[2,3],[1,5,1]]))
print(max_weight([[1],[2,3],[1,5,1],[100,5,6,9]]))
print(max_weight_dp([[1],[2,3],[1,5,1],[100,5,6,9]]))
