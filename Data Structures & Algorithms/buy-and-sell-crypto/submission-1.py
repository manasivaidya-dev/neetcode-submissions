class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left,right, maxdiff = 0,0,0
        while right < len(prices)-1:
            right += 1
            diff = prices[right] - prices[left]
            if diff > maxdiff:
                maxdiff = diff
            if diff < 0:
                left = right
        return maxdiff


        