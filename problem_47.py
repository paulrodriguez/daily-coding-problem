'''
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made 
from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''


def buy_sell_stock(arr):
    best_buy = float('inf')
    max_profit = 0
    for n in arr:
        if n < best_buy:
            best_buy = n
        else:
            max_profit = max(max_profit,n - best_buy)
    return max_profit



assert buy_sell_stock([9,11,8,5,7,10]) == 5
assert buy_sell_stock([1,2,3,4,5,7,0,4]) == 6
