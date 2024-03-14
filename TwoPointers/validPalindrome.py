# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
s = "A man, a plan, a canal: Panama"

# Solution 1


def isPalindrome(s: str) -> bool:
    s = s.lower()
    # Check all char one by on and add it to a new string if it's Alpha-numemric
    cleanS = ''.join(c for c in s if c.isalnum())
    # cleanS[::-1] create a reverse list. Will take all list [::] but starting from -1 (end of list)
    if cleanS == cleanS[::-1]:
        return True
    else:
        return False


class Solution:
    def isPalindrome(s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True


print(Solution.isPalindrome(s))
