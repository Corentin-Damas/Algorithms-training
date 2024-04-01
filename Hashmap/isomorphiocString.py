class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        dict01, dict02 = {}, {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in dict01 and dict01[c1] != c2) or (c2 in dict02 and dict02[c2] != c1)):
                return False
            dict01[c1] = c2
            dict02[c2] = c1
        return True
            
        

str01 = "paper"
str02 = "title"

print(Solution.isIsomorphic(str01,str02 ))

