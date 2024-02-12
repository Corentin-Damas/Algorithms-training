from typing import List


class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        i = 0
        last = len(nums) - 1
        while not i > last:
            if nums[i] == val:
                nums.pop(i)
                last -= 1
            else:
                i += 1
        return i


case01 = [3, 2, 2, 3]
print(Solution.removeElement(nums=case01, val=3))
case02 = [0, 1, 2, 2, 3, 0, 4, 2]
print(Solution.removeElement(nums=case02, val=2))
