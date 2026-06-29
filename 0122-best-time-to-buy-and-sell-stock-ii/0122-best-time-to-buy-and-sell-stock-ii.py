class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                max_profit += profit

        return max_profit


        
