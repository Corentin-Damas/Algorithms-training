#188. Best Time to Buy and Sell Stock IV
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        N = len(prices)
        dp = [0]*N
        
        if k > N:
            B = [prices[i]- prices[i-1] for i in range(1,N)]
            return sum(b for b in B if b> 0)
        
        for t in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, N):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, pos +prices[i])
                dp[i] = profit
        
        return dp[-1]