
# Given an integer array nums sorted in non-decreasing order, remove some duplicates 
# in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

from typing import List

class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        leftP = 1
        occurance = 1
        
        for rightP in range(1, len(nums)):
            if nums[rightP] == nums[rightP -1]:
                occurance +=1
            else: 
                occurance = 1
            
            if occurance <= 2:
                nums[leftP] = nums[rightP]
                leftP += 1

        
        return leftP
    


case_01 = [1,1,1,2,2,3]
case_02 = [0,0,1,1,1,1,2,3,3]

print(Solution.removeDuplicates(case_01)) 
print(Solution.removeDuplicates(case_02)) 