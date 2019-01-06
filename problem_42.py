'''
Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.
'''
# brute force approach using backtracking
def subset(arr,k):
    start = 0
    res = []

    if util(arr,k,start,res) == True:
        return res

    return []

def util(arr,k,start,res):
    if k == 0:
        return True

    for i in xrange(start,len(arr)):
        target = k - arr[i]
        if target>=0:
            res.append(arr[i])

            if util(arr,target,i+1,res)==True:
                return True

            res.pop()
    return False
            
# dynamic programing approach
def subsetv2(arr,k):
    dp = [[False]*(k+1) for _ in xrange(len(arr))]
    
    for i in xrange(len(arr)):
        dp[i][0] = True
    
    

    for j,n in enumerate(arr):
        end = min(n,k+1)

        for i in xrange(1,end):
            dp[j][i] = dp[j-1][i] if j>0 else False


        for i in xrange(end,k+1):
            if dp[j-1][i-n] == True or dp[j-1][i] == True:
                dp[j][i] = True
            else:
                dp[j][i] = False

    if dp[-1][-1] == False:
        return None

    #print(dp)
    res = []
    row = len(arr)-1
    col = k
    while row >0:
        if dp[row-1][col] == False and dp[row][col] == True:
            res.append(arr[row])
            row -= 1
            col -= arr[row]
        else:
        if dp[row-1][col] == True:
            row -= 1
        else:
            if (col-arr[row])>=0:
                res.append(arr[row])
                row -= 1
                col -= arr[row]
            else:
                row += 1
                col += res.pop()
        print(col)

    print(res)
subsetv2([12,1,61,5,9,2],24)
        
assert sorted(subset([12,1,61,5,9,2],24)) == sorted([12,9,2,1])

