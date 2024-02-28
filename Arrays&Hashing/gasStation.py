from typing import List

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


class Solution:
    # Work but time limit exceeded on really big arrays
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        lenArr = len(gas)
        if lenArr == 1 and gas[0] >= cost[0]:
            return 0
        dif = []
        for i in range(lenArr):
            dif.append(gas[i] - cost[i])

        for idxD, d in enumerate(dif):
            if d <= 0:
                continue
            else:
                tank = 0
                for p in range(0, lenArr):
                    tank += dif[(idxD+p) % lenArr]
                    if tank < 0:
                        break
                if tank < 0:
                    continue
                if tank >= 0:
                    return idxD
    # Greedy
    def canCompleteCircuit_02(gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i]- cost[i])
            
            if total < 0:
                total = 0
                res = i + 1
        return res

gaz01 = [1, 2, 3, 4, 5]
cost01 = [3, 4, 5, 1, 2]

print(Solution.canCompleteCircuit(gaz01, cost01))
