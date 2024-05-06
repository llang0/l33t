# 121. Best Time to Buy and Sell a Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    maxProfit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[left] < prices[right]:
            maxProfit = max(maxProfit, prices[right]-prices[left])
        else: 
            left = right
        right += 1

    return maxProfit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))