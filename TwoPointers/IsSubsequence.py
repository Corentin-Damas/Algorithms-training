class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        pointS = 0
        if len(s) == 0:
            return True
        
        
        for l in t:
            if l == s[pointS]:
                pointS += 1   
                if pointS == len(s):
                    return True
        
        return False
              
        
        
        


print(Solution.isSubsequence("ace", "aec"))