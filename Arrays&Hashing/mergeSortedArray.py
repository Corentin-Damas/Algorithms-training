from typing import List
class Solution:
    def __init__(self, nums1, m, nums2, n) -> None:
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """       
        pLast = (m + n)-1
        while m > 0 and n > 0 :
            if nums1[m-1] > nums2[n-1]:
                nums1[pLast] = nums1[m-1]
                m-=1
            
            else:
                nums1[pLast] = nums2[n-1]
                n -= 1
            pLast -=1
        while n > 0:
            nums1[pLast] = nums2[n-1]
            n, pLast = n-1, pLast -1
    def solution(self):
        return self.nums1


li1 = [1,2,3,0,0,0]
a = 3
li2 = [2,5,6]
b =3

solution = Solution(li1, a, li2, b)
solution.merge(solution.nums1, solution.m, solution.nums2, solution.n)
result= solution.nums1

print(result)