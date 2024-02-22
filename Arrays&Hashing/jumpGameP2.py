# This time You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i.

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]

from typing import List


class Solution:
    # Work but is very time consuming breadth first search type of solution
    # Dynamic programing Solution
    def jump(nums: List[int]) -> bool:
        if len(nums) == 1:
            return 0
        if nums[0] == 0:
            return 0

        count = 0
        # memo = {}

        queue = [[nums]]
        while len(queue) >= 1:
            count += 1
            testedLvl = queue.pop(0)
            lvl = []

            for testedArr in testedLvl:
                jumpSize = testedArr[0]

                if jumpSize >= len(testedArr):
                    return count

                for j in range(jumpSize, 0, -1):

                    if testedArr[j:] in lvl:
                        continue
                    if len(testedArr[j:]) == 1:
                        return count

                    lvl.append(testedArr[j:])
            print(lvl)
            queue.append(lvl)

    # Greedy solution
    # We are going throuth the array by looking only at the lenght of the jump leftP[possibleValues]rightP and updating that lenght everytime by looking at the possible values
    def jump2(nums: List[int]) -> bool:
        nbJump = 0
        leftP = rightP = 0
        while rightP < len(nums)-1:
            farthestJump = 0
            for i in range(leftP, rightP + 1):
                # update the max jump compare actual farthest and the value pointed by l[rangeOfVals]r
                farthestJump = max(farthestJump, i + nums[i])
            # Goes to the next possible section
            leftP = rightP + 1
            rightP = farthestJump
            nbJump += 1
        return nbJump
                
            


case01 = [2, 3, 1, 1, 4]
case02 = [3, 2, 0, 1, 4]

case04 = [4, 1, 0, 2, 2, 4, 4, 4, 1, 2]
print(Solution.jump(case01))
print(Solution.jump(case02))
print(Solution.jump(case04))
