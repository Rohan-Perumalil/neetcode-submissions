class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = max_profit = 0
        
        for R in range(1, len(prices)):
            profit = prices[R] - prices[L]
            if profit >= 0:
                max_profit = max(profit, max_profit)
            else:
                L = R
        
        return max_profit