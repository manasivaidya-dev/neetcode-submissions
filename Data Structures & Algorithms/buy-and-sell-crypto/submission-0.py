class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
                right = i
            if prices[i] > prices[right]:
                right = i
            profit = prices[right] - prices[left]
            max_profit =max(max_profit, profit)
        return max_profit

        