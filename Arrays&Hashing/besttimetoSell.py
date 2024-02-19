from typing import List

class Solution:
    #Runtime 729ms(best than 77.90%) Memory 27.42MB (best than 67.51%)  
    def maxProfit(prices: List[int]) -> int:
        best = 0
        leftP, rightP = 0, 1
        while rightP < len(prices):
            if  prices[leftP] > prices[rightP]:
                leftP = rightP
            elif best < (prices[rightP] - prices[leftP]):
                best =  prices[rightP] - prices[leftP]
            rightP+=1        
        return best
    

case_01 =[7,1,5,3,6,4]
case_02 =[7,6,4,3,1]


print(Solution.maxProfit(case_01))
print(Solution.maxProfit(case_02))