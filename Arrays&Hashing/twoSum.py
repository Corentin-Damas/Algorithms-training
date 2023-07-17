# Two Sum

# Instructions:
# Given an array of integers "nums" and an integer "target", 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# Comments:
# Both nums and target are set by us, target is the result 
# of a Sum (2 or more num involved) of nums in the array 

nums = [3, 56, 10, 2, 5, 8, 19, 28]
target = 18



def twoSum(nums:list[int], target: int):
    dictAnswer = {}     # dict where will be map {the value of num: index}
    
    for idx, value in enumerate(nums):
        diff = target - value 
        if diff in dictAnswer:
            # we check in the dictionny of the previously tested value if the remaining is in there if the remaing is in there we got our two Sums 
            # exemple: 18 - 8 = 10, if there is a 10 that we already tested meaning that 8 + 10 = 18(target) 
            
            return (dictAnswer[diff], idx) # return previously tested index and the index of the value actually tested
        
        # Add to the dict the tested value and pass to the next loop
        dictAnswer[value] = idx
    return

print(twoSum(nums, target))