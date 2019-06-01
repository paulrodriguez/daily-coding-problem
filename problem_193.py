'''
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock.
You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like
'''


def maxProfit(arr,fee):

    buy = [0]*len(arr)
    sell = [0]*len(arr)

    buy[0] = -arr[0]

    for i in range(1,len(arr)):
        buy[i] = max(buy[i-1],-arr[i] + sell[i-1])
        sell[i] = max(arr[i] - fee + buy[i-1], sell[i-1])


    return sell[-1]

print(maxProfit([1,3,2,8,4,10],2))
print(maxProfit([1,2,3,4,5,6,7,8,9],2))
