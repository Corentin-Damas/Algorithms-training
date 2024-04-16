from typing import List


class Solution:
    def summaryRanges(nums: List[int]) -> List[str]:
        #answer probably to clumsy
        l, r = 0, 1
        res = []
        while r  < len(nums):
            if nums[r - 1] == nums[r] - 1:
                r+=1
                continue
            elif nums[r - 1] != nums[r] - 1 and l == r - 1:
                res.append("%s"%(nums[l]))
                l+=1
                r+=1
            else:
                res.append("%s->%s"%(nums[l],nums[r-1]))
                l = r
                r +=1
        
        if l == len(nums)-1:
            res.append("%s"%(nums[l]))
        elif r == len(nums):
            res.append("%s->%s"%(nums[l],nums[r-1]))
        
        return res
    
    
    
    

case01 = [0,2,3,4,6,8,9]
print(Solution.summaryRanges(case01))