class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t=0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            t+= max(diff,0)
        return t