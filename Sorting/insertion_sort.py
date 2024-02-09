# O(n^2)

# Simple implementation, easy to write
# Fast for very small data sets
# Faster than other simple sorting algorithms like Bubble Sort
# Adaptive: Faster for partially sorted data sets
# Stable: Does not change the relative order of elements with equal keys
# In-Place: Only requires a constant amount of memory
# Online: Can sort a list as it receives it

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
            j -= 1
    return nums