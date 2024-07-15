# 153. Find Minimum in Rotated Sorted Array
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l+ (r-l) //2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[l] <= nums[mid] and nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid -1
                
                
        return nums[l]
                
            
        