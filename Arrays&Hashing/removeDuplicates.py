from typing import List


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
# that each unique element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.


class Solution:
    # Runtime 133ms Memory 18.22MB
    def removeDuplicates(nums: List[int]) -> int:
        idx = 0
        lenNum = len(nums)
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                nums.pop(idx+1)
                lenNum -= 1
            else:
                idx += 1
        return lenNum

    # Runetime 68ms Memory 18.08MB
    def removeDuplicatesV2(nums: List[int]) -> int:
        # leftPointer his job is to clean the array, keep track of the idx where the number should be change so that the first nums are all different
        # and will be the lenght of the final array
        # rightPointer will keep track of the numbers of duplications
        leftP, rightP = 1, 1

        for i in range(len(nums)-1):
            if nums[i] == nums[rightP]:
                rightP += 1
            else:
                nums[leftP] = nums[rightP]
                leftP += 1
                rightP += 1

        return leftP


case_01 = [1, 1, 2]
case_02 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# print(Solution.removeDuplicates(case_01))
# print(Solution.removeDuplicates(case_02))

print(Solution.removeDuplicatesV2(case_01))
print(Solution.removeDuplicatesV2(case_02))
