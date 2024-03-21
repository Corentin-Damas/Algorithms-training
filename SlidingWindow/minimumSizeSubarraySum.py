from typing import List


class Solution:
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        wind = 0
        res = float("inf")

        while r < len(nums):
            wind += nums[r]
            while wind >= target:
                res = min(r - l + 1, res)
                wind -= nums[l]
                l += 1
            r+= 1

        return 0 if res == float("inf") else res


case01 = [2, 3, 1, 2, 4, 3]
print(Solution.minSubArrayLen(7, case01))
