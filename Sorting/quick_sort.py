def quick_sort(nums, low, high):
    if low < high:
        nums, i = partition(nums, low, high)
        nums = quick_sort(nums, low, i-1)
        nums = quick_sort(nums, i+1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return nums, i
