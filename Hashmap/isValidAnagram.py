class Solution:
    def isAnagram(s: str, t: str) -> bool:
        letterDic= {} 
        for letter in s:
            if letter in letterDic:
                letterDic[letter] += 1
            else:
                letterDic[letter] = 1
        
        for l in t:
            if l in letterDic:
                letterDic[l] -=1
            else: return False

        for key, val in letterDic.items():
            if val != 0:
                return False
        
        return True
            
    

print(Solution.isAnagram("anagram", "nagaram"))