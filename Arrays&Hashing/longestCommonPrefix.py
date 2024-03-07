from typing import List


class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
            
        

case01 = ["flower", "flow", "flight"]
case02 = ["dog", "racecar", "car"]
case03 = ["ab", "a"]

print(Solution.longestCommonPrefix(case03))
