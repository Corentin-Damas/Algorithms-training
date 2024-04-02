class Solution:
    def wordPattern(pattern: str, s: str) -> bool:
        chToW = {}
        wToCh = {}
        arrString = s.split(" ")
        if len(pattern) != len(arrString):
            return False

        for c, w in zip(pattern, arrString):
            if c in chToW and chToW[c] != w:
                return False
            if w in wToCh and wToCh[w] != c:
                return False
            chToW[c] = w
            wToCh[w] = c
        return True
