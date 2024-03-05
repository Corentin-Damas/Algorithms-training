class Solution:
    def intToRoman(num: int) -> str:
        table = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], [
            "XC", 90], ["CD", 400], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        res = ""

        for sym, val in reversed(table):
            if num // val:
                count = num // val
                res += (sym*count)
                num = num % val
        return res


# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
case01 = "3"
case02 = "58"
case03 = "1994"

print(Solution.romanToInt(case01))
