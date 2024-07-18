# 502. IPO
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxPRofit = []
        minCapital = [(c,p)for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        
        for i in range(k):
            while minCapital and minCapital[0][0]<= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxPRofit, -1 *p)
            if not maxPRofit:
                break
            w += -1 *heapq.heappop(maxPRofit)
        return w