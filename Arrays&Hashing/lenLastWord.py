
class Solution:
    def lengthOfLastWord(s: str) -> int:
        arr = s.split()
        return len(arr[-1])

    def lengthOfLastWordV2(s: str) -> int:
        s = s.strip()
        last_idx = len(s) - 1
        i = len(s) - 1

        while i >= 0 and s[i] != ' ':
            i -= 1
        return last_idx - i

    def lengthOfLastWordV3(s: str) -> int:
        i = len(s) - 1
        while i > 0 and s[i] == ' ':
            i -= 1
        last_idx = i

        while i >= 0 and s[i] != ' ':
            i -= 1
        return last_idx - i


case01 = "luffy is still joyboy"

print(Solution.lengthOfLastWordV3(case01))
