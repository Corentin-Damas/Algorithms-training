from typing import List


class Solution:
    
    def maxProfit(prices: List[int]) -> int:
        if(prices==sorted(prices)):
            return(max(prices)-min(prices))
        elif(prices==sorted(prices)[::-1]):
            return 0
        else:
            maxProfit = 0
            for i in range (len(prices) -1):
                # everyday we are adding up adding up the profit 
                if prices[i+1] > prices[i]:
                    maxProfit += prices[i+1] - prices[i]
            return maxProfit
                   




case01 = [7,1,5,3,6,4]
case02 = [1,2,3,4,5]
case03 = [7,6,4,3,1]

print(Solution.maxProfit(case01))
print(Solution.maxProfit(case02))
print(Solution.maxProfit(case03))