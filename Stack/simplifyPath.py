class Solution:
    def simplifyPath(path: str) -> str:
        stack = []
        curFile = ""
        for c in path + "/":
            if c == "/":
                if curFile == "..":
                    if stack:
                        stack.pop()
                elif curFile != "" and curFile != ".":
                    stack.append(curFile)

                curFile = ""

            else:
                curFile += c

        return "/"+"/".join(stack)
