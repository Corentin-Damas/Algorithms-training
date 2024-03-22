from typing import List

class Solution:
    #Not the most optimal because oh the second while loop i use to compensate the use of 2 pointers (i used only one in that exemple)
    def lengthOfLongestSubstring( s: str) -> int:
        r = 0
        maxL = 0
        wind = []
        
        if len(s) == 1:
            return 1
        
        while r < len(s):
                            
            if s[r] not in wind:
                wind.append(s[r])
                r+=1

            elif s[r] in wind:
                maxL = max(len(wind), maxL )
           
                while s[r] in wind:
                    wind.pop(0)
                    
                
        
        maxL = max(len(wind), maxL )      
        return maxL
             
    
case01="abcabcbb"

print(Solution.lengthOfLongestSubstring(case01))
    