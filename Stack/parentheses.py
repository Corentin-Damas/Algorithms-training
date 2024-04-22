class Solution:
    def isValid(s: str) -> bool:
        stack = []
        types = {")": "(",
                 "}": "{",
                 "]": "["}

        for symb in s:

            if symb in types:
                if stack and types[symb] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(symb)

        if len(stack) == 0:
            return True
        else:
            return False
