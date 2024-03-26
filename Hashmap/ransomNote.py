class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        hashMag = {}
        for l in magazine:
            if l in hashMag:
                hashMag[l] += 1
            else:
                hashMag[l] = 1

        for r in ransomNote:
            if r not in hashMag or hashMag[r] == 0:
                return False
            else:
                hashMag[r] -= 1
        return True


print(Solution.canConstruct("aa", "aab"))
