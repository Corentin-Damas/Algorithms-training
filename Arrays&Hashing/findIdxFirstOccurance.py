# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(haystack: str, needle: str) -> int:
        p = 0
        lenN = len(needle)
        while p <= len(haystack) - lenN:
            if haystack[p:p+lenN] == needle:
                return p
            p+=1
        return -1



print(Solution.strStr("a", "a"))