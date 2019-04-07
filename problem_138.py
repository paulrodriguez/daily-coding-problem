'''
Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
'''

def makeChange(n):
    coins = [1,5,10,25]

    dp = [float('inf')]*(n+1)
    dp[0] = 0

    for i in range(1,n+1):
        for c in coins:
            target = i - c
            if target>=0:
                dp[i] = min(dp[i],+dp[target]+1)
    
    return dp[n]


assert makeChange(16) == 3
assert makeChange(25) == 1
assert makeChange(50) == 2
assert makeChange(75) == 3
assert makeChange(74) == 8

assert makeChange(76) == 4
assert makeChange(102) == 6 
