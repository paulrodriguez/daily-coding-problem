'''
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. 
You and an opponent take turns choosing either the first or last coin from the row,
 removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, 
assuming your opponent plays optimally.
'''

def maxMoney(coins):
	if len(coins) == 0:
		return 0
	if len(coins) <=2:
		return max(coins)

	dp = [[0]*len(coins) for _ in range(len(coins))]

	for i in range(len(coins)):
		dp[i][i] = coins[i]

	for i in range(len(coins)-1):
		dp[i][i+1] = max(coins[i],coins[i+1])

	for size in range(3,len(coins)):
		for i in range(len(coins)-size):
			j = i + size

			dp[i][j] = max(coins[i]+min(dp[i+2][j-1],dp[i+1][j-2]),
				coins[j] + min(dp[i+1][j-1],dp[i][j-2]))
	return dp[0][len(coins)-1]

print(maxMoney([5,7,4,1,3,4]))
print(maxMoney([5,3,7,10]))
print(maxMoney([8,15,3,7]))
print(maxMoney([2,2,2,2]))
print(maxMoney([20,30,2,2,2,10]))
