class Solution:
    def reverseWords(s: str) -> str:
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)
        

case01 = "the sky is blue"

print(Solution.reverseWords(case01))