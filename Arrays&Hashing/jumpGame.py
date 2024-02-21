# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
from typing import List


class Solution:
    def canJump(nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False


        # rightP is the current maximum index we can reach
        rightP = 0
        last = len(nums) - 1

        for idx in range(len(nums)):
            # test case where our potentiel max index can't go futher and is block at the previous step
            # [3, 2, 1, 0, 4]
            #  at i = 3 rightP = 3+0  i= 4 rightP = 3 can't reach idx 4
            if idx > rightP:
                return False

            # if we arrive on a inx that can increase our range (rightP)
            if nums[idx] + idx > rightP:
                rightP = nums[idx] + idx

            # if our right Pointer goes beyound the lenght of the array = we can jump to that position
            if rightP >= last:
                return True


case01 = [2, 3, 1, 1, 4]
case02 = [3, 2, 1, 0, 4]
case03 = [3, 0, 8, 2, 0, 0, 1]

case04 = [4, 1, 0, 2, 2, 4, 4, 4, 1, 2]
print(Solution.canJump(case01))
print(Solution.canJump(case02))
print(Solution.canJump(case03))
print(Solution.canJump(case04))
