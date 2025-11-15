class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = 0
        max_profit = 0
        cur_profit = 0
        for i in range(len(prices)):
            cur_price = prices[i]
            if cur_price < prices[buy]:
                buy = i
                if sell<buy:
                    sell = i 
            elif cur_price > prices[sell]:
                sell = i
                if buy > sell:
                    buy = i
            cur_profit = prices[sell]-prices[buy]
            max_profit = max(cur_profit, max_profit)
        return max_profit

# Leetcode Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/