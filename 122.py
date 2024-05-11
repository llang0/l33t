# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def maxProfit(prices):
    maxProfit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[left] < prices[right]:
            maxProfit += prices[right]-prices[left]

        left = right
        right += 1

    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))