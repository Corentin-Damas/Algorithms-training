class Solution:
    def convert(s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for idx in range(numRows):
            baseJump = (numRows - 1) * 2
            for i in range(idx, len(s), baseJump):
                res += s[i]
                if (idx > 0 and idx < numRows - 1 and i + baseJump - 2*idx < len(s)):
                    res += s[i + baseJump - 2*idx]
        return res


case01 = "PAYPALISHIRING"

print(Solution.convert(case01, 3))
print(Solution.convert(case01, 4))
