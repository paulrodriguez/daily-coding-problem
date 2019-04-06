'''
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
'''

# TODO: find a more optimized solution
# solution below does not work
def largestRectangle(arr):
    area = 0
    for i in xrange(arr):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] == 0:
                j += 1
                continue
            k = j + 1
            while k < len(arr[i]):
                if arr[i][k] == 0:
                    break
                
            
            
    pass


rect = [[1,0,0,0],[1,0,1,1],[1,0,1,1],[0,1,0,0]]
assert largestRectangle(rect) == 4


