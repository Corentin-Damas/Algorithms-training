from typing import List


class Solution:
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = res[-1][1] # Get the max value of the last interval added
            
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end) # Update the interval max value
            else:
                res.append([start, end])
        return res
        


case01 = [[1,3],[2,6],[8,10],[15,18]]
print(Solution.merge(case01))