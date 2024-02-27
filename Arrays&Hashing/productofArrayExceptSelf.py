from typing import List
import math
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    # First attmpt , works but not for very large arrays
    def productExceptSelf(nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            p1 = nums[:i]
            p2 = nums[i+1:]
            result.append(math.prod(p1+p2))
        
        return result
    # Second atempt O(n) space O(1)
    def productExceptSelf_02(nums: List[int]) -> List[int]:
        #for each cells we mutliply all the element comming before it [prefix] 
        #then we do the same but by reversed order. [postfix]
        # the result for each cells is the multiplication of this 2 result 
        pre = 1
        output = []
        for i in nums:
            output.append(pre)
            pre *= i 
        pre = 1
        for idx in range(len(nums)-1, -1, -1):
            output[idx] *=pre
            pre *=nums[idx] 
        
        return output
            
            
            
            






case01 = [1,2,3,4]
print(Solution.productExceptSelf_02(case01))