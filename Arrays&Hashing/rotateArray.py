from typing import List

# Run time 158ms , Memory 27.99MB
class Solution:
    # Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenArr = len(nums)
        tempList = nums.copy()
        last = 0
        for i in range(0, lenArr):
            next = ((i+k) % lenArr)
            nums[next] = tempList[i]

        print(nums)


case_01 = [1, 2, 3, 4, 5, 6, 7]
k = 3

Solution.rotate(case_01, k)
