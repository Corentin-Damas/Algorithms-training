# Given an integer array nums, return true if any value appears at least twice 
#  in the array, and return false if every element is distinct.

nums = [1, 2, 3, 5, 2]


def containDuplicate(nums:list[int]) -> bool:
    numsMap = {}
    
    for el in nums:
        # Initialize the map assign 0 to num, if there is a duplicate will get +1
        numsMap[el] = numsMap.get(el, 0) +1 

    for k in numsMap:
        # Check if any key value paire of the Map has been counted more than 2 time
        if numsMap[k] > 1: return True
    return False
 
print(containDuplicate(nums))
