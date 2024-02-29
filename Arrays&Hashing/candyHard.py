from typing import List


class Solution:
    def candy(ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candy = [1] * len(ratings)
        leftP = 0
        rightP = 1
        while rightP < len(ratings):
            if ratings[rightP] > ratings[leftP]:
                candy[rightP] = candy[leftP] + 1
            leftP += 1
            rightP +=1
            print(candy)
        
        leftP -= 1
        rightP -=1
        
        while leftP >= 0:
            if ratings[leftP] > ratings[rightP]:
                candy[leftP] = max(candy[leftP], candy[rightP] + 1 )
            leftP -= 1
            rightP -=1

        return sum(candy)
    

case01 = [1,0,2]
case02 = [1,2,2]
case03 = [5,4,3,5,6,2]

print(Solution.candy(case01))
print(Solution.candy(case02))
print(Solution.candy(case03))