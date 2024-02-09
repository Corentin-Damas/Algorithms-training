# O(n^2)

import random

def bubble_sort(nums):
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    return nums


def test(nums):
    res = bubble_sort(nums.copy())
    print(f"nums: {nums}")
    print(f"sorted: {res}")
    print("====================================")


def get_nums(num):
    nums = []
    random.seed(0)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


def main():
    test(get_nums(9))
    test(get_nums(20))


main()
