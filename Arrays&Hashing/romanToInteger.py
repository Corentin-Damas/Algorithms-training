class Solution:
    def romanToInt(s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s = s[::-1]

        result = 0
        last = ""
        for sym in s:
            if sym == "I" and (last == "V" or last == "X"):
                result -= table[sym]
                continue
            elif sym == "X" and (last == "L" or last == "C"):
                result -= table[sym]
                continue
            elif sym == "C" and (last == "D" or last == "M"):
                result -= table[sym]
                continue
            
            
            result += table[sym]
            last = sym
        return result

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


case01 = "III"
case02 = "LVIII"
case03 = "MCMXCIV"
case04 = "CIIV"

print(Solution.romanToInt(case04))
