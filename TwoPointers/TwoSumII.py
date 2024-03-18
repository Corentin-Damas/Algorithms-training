from typing import List


class Solution:
    # First try
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while numbers[l] == numbers[r] and numbers[l] + numbers[r] != target:
            l += 1
            r += 1

        while numbers[l] + numbers[r] != target:
            r += 1
            if len(numbers) == r:
                l += 1
                r = l+1
        return [l+1, r+1]

    def twoSum_02(numbers: List[int], target: int) -> List[int]:
        # Optimized
        l, r = 0, len(numbers) - 1
        while l < r != target:
            res = numbers[l] + numbers[r]

            if res == target:
                return [l+1, r+1]
            elif res < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]


print(Solution.twoSum([2, 7, 11, 15], 9))
print(Solution.twoSum([5, 25, 75], 100))
