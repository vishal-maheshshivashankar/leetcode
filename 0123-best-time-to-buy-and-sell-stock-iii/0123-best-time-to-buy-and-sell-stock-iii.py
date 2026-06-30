class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        # LEFT: best profit from 1 transaction on days 0 to i
        left = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i-1], prices[i] - min_price)
        
        # RIGHT: best profit from 1 transaction on days i to n-1
        right = [0] * n
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i+1], max_price - prices[i])
        
        # Find best split point
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])
        
        return max_profit