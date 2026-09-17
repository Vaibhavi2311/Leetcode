class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        max_pro=0
        min_price=float("inf")
        for i in range(0,n):
           min_price=min(min_price,prices[i])
           max_pro=max(max_pro,prices[i]-min_price)
        return max_pro
    