from typing import List

#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(height: List[int]) -> int:
        if len(height)<3 :return 0
        
        leftP = 0
        rightP = len(height) -1
        leftMax = height[leftP]
        rightMax = height[rightP]
        water = 0
        
        while leftP < rightP:
            if leftMax < rightMax:
                leftP += 1
                leftMax = max(leftMax, height[leftP])
                curr = leftMax - height[leftP]
                if curr >= 0:
                    water += curr
                
            else:
                rightP-=1
                rightMax = max(rightMax, height[rightP])
                curr = rightMax - height[rightP]
                if curr >= 0:
                    water += curr
        return water
        
        
         
    
case01 = [0,1,0,2,1,0,1,3,2,1,2,1]        
case02 = [4,2,0,3,2,5]


print(Solution.trap(case01))        
print(Solution.trap(case02))        