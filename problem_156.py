'''
Given a positive integer n, find the smallest number of squared integers which sum to n.
'''
import math
'''
space complexity: O(n)
a list is created for the loop on each recursive step

time complexityL O(2^n)
it creates a recursive call at each iteration in the loop
'''
def smallest_squared_integers(num):
    max_squared = int(math.sqrt(num)) + 1
    #print(max_squared)
    return rec(num,0,max_squared)

def rec(num,count,start):
    if num == 0:
        return count

    curr_count = float('inf')
    for i in range(start,0,-1):
        squared = i*i
        if squared > num:
            continue
        
        curr_count = min(curr_count,rec(num-squared,count+1,i))

    return curr_count


'''
space complexity O(n)
n is the number we are trying to find the solution for

time complexity O(n^2)
need two loops: the first will go through numbers from 1 up to n to find
their solutions
the second recurses from the max squared number of the number iterator
in the parent loop down to 1
'''
def smallest_squared_integersv2(num):
    if num <=0:
        return 0

    dp = [float('inf')]*(num+1)
    dp[0] = 0    
    for i in range(1,num+1):
        max_squared = int(math.sqrt(i))+1
        for j in range(max_squared,0,-1):
            diff = i - j*j
            if diff < 0:
                continue
            dp[i] = min(dp[i],dp[diff] + 1)
    return dp[num]

assert smallest_squared_integers(13) == 2
assert smallest_squared_integersv2(13) == 2
assert smallest_squared_integers(27) == 3
assert smallest_squared_integersv2(27) == 3
assert smallest_squared_integers(80) == 2
assert smallest_squared_integersv2(80) == 2
assert smallest_squared_integers(81) == 1
assert smallest_squared_integersv2(81) == 1
assert smallest_squared_integers(101) == 2
assert smallest_squared_integersv2(101) == 2
assert smallest_squared_integers(103) == 4
assert smallest_squared_integersv2(103) == 4
assert smallest_squared_integers(104) == 2
assert smallest_squared_integersv2(104) == 2
assert smallest_squared_integers(144) == 1
assert smallest_squared_integersv2(144) == 1
