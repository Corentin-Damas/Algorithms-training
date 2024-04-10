from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, nu in enumerate(nums):
            diff = target - nu
            if diff in numDict:
                return [numDict[diff], idx]
            numDict[nu] = idx
        return 


print(Solution.twoSum([3,3], 6))
