# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

#An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

s1 = "()"
s2 = "()[]{}"
s3 = "[{}()]"
s4 = "[{}())"

# attenpt 1
def isValid(s: str) -> bool:
    # 
    parenthesesTypes = {")": "(",
                        "]": "[",
                        "}": "{",}
    stack = []  # will be populated with open brackets, should be empty to be True, each time a closing bracket has a corresponding 
                # open bracket in the stack it should be removed from the stack 
    
    for c in s:
        if c in parenthesesTypes: # take care of closing bracket
            # if the stack exist and that the last open bracket is corresponding to the actual tested closing tag remove the open tag from stack
            if stack and stack[-1] == parenthesesTypes[c]:
                stack.pop()
            else: # if there is no match in the stack for the  tested closing bracket : return false
                return False
        else:  # take care of only adding open bracket to the stack
            stack.append(c) 
    return True if not stack else False

print(isValid(s3))

