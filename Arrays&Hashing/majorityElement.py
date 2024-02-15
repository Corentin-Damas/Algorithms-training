from typing import List


# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    # Runtime 143 ms Memory 17.99
    def majorityElement(nums: List[int]) -> int:
        numDic = {}
        for i in nums:
            if i in numDic.keys():
                numDic[i] += 1
            else:
                numDic[i] = 1
        for k, v in numDic.items():
            if v >= len(nums)/2:
                return k
        return 0
    
    # Runtime 128ms  Memory 17.99
    def majorityElementv2(nums: List[int]) -> int:
        curr = None
        count = 0
        for n in nums:
            if count == 0:
                curr = n
            if n == curr: 
                count += 1
            else: 
                count -1
        return curr
        


case_01 = [3,2,3]
case_02 = [2,2,1,1,1,2,2]

print(Solution.majorityElement(case_01))
print(Solution.majorityElement(case_02))