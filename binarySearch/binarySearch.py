# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

nums1 = [-1,0,3,5,9,12]
target1 = 9

def search(nums: list[int], target: int) -> int:
    # nums arrays of number, target number, search return index number
    min = 0
    max = len(nums)
        
    while min <= max:
        mid = (max + min)//2 # by the average or by "distance" -> mid = min+((max-min)//2)
        print("middle =",mid, " min:", min, "max:", max)

        if nums[mid] < target:
            min = mid + 1 # we already check if this mid = target it's not so we can remove it also from the search
            print("new min: ", min)
            
        if nums[mid] > target:
            max = mid - 1
            print(" new max: ", max)

        if nums[mid] == target:
            print("idx found: ", mid)
            return mid

    print(nums[0])
    return nums[0]
# search(nums1, target1)
search([-1,0,3,5,9,12], 2)