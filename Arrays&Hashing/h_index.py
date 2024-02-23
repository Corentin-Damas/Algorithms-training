from typing import List


class Solution:
    def hIndex(citations: List[int]) -> int:
        if len(citations) <= 1 and citations[0] == 0:
            return 0
        if len(citations) == 1:
            return 1

        citations.sort(reverse=True)
        if citations[-1] >= len(citations):
            return len(citations)

        for idx, countCitation in enumerate(citations):
            if idx+1 == countCitation:
                return idx+1
            if countCitation < idx+1:
                return idx
        return 0

    def hIndex2(citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        while h < len(citations) and citations[h] > h:
            h += 1
        return h


case01 = [3, 0, 6, 1, 5]  # [ 6, 5, 3, 1, 0]
case02 = [1, 3, 1]  # [3, 1, 1]

print(Solution.hIndex(case01))
print(Solution.hIndex(case02))
