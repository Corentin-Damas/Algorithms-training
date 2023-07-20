# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

s = " "
def isPalindrome(s:str)->bool:
    s = s.lower()
    # Check all char one by on and add it to a new string if it's Alpha-numemric  
    cleanS = ''.join(c for c in s if c.isalnum()) 
    # cleanS[::-1] create a reverse list. Will take all list [::] but starting from -1 (end of list)
    if cleanS == cleanS[::-1]: return True
    else: return False


print(isPalindrome(s))
        