from typing import List

class Solution:
    def maxArea(height: List[int]) -> int:
        l = 0
        r = len(height)-1
        curr= 0
        
        while r > l:
            temp = min(height[l], height[r]) * (r - l)
            if temp > curr:
                curr = temp
            
            if height[l] > height[r]:
                r-=1
            else :
                l+=1
        
        return curr
            
        
        
         
    
print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))
        