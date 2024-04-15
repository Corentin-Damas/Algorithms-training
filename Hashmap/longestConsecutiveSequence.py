from typing import List


class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        # Too slow for very large set of data
        dictNums = {}
        for num in nums:
            dictNums[num] = 0

        res = 0
        for n in nums:
            count = 0
            if dictNums[n] == 1:
                continue
            while n+count in dictNums:
                dictNums[n+count] += 1
                count += 1
            if count > res:
                res = count
        return res

    def longestConsecutive_02(nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                res = max(length, res)
        return res


case01 = [100, 4, 200, 1, 3, 2]
print(Solution.longestConsecutive_02(case01))
