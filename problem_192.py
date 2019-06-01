'''
You are given an array of nonnegative integers.
Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.
'''

'''
Space Complexity: O(n^2)
using a 2d array

Time Complexity: O(n^2)
checking previous elements to see if we could get from them, and 
settings values of ahead elements that we can get to
'''
def canGetToEnd(arr):

    dp = [[False]*len(arr) for _ in range(len(arr))]

    cols = len(arr)
    rows = len(arr)
    dp[0][0] = True
    
    for i in range(len(arr)):
        n = arr[i]

        j = i - 1
        while j > -1:
            if dp[j][i] == True:
                dp[i][i] = True
                break
            j -= 1
        if dp[i][i] == False:
            continue

        while n > 0:
            if (i+n) < cols:
                dp[i][i+n] = True
            n -= 1

    return dp[-1][-1]    

    
    


assert canGetToEnd([1,3,1,2,0,1]) == True
assert canGetToEnd([1,1,1,1,1,1]) == True
assert canGetToEnd([1,2,0,0,1,1]) == False
assert canGetToEnd([1,3,0,0,1,1]) == True
assert canGetToEnd([1,2,1,0,0])   == False
