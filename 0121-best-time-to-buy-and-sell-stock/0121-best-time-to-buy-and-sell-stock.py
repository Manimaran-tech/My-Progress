class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        profit = 0
        for i in range(len(prices)):
            minSoFar = min(minSoFar, prices[i])
            profit = max(profit, prices[i] - minSoFar)
        return profit