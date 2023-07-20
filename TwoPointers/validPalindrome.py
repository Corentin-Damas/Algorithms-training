# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
s = "A man, a plan, a canal: Panama"

# Solution 1
def isPalindrome(s:str)->bool:
    s = s.lower()
    # Check all char one by on and add it to a new string if it's Alpha-numemric  
    cleanS = ''.join(c for c in s if c.isalnum()) 
    # cleanS[::-1] create a reverse list. Will take all list [::] but starting from -1 (end of list)
    if cleanS == cleanS[::-1]: return True
    else: return False
    
#Solution 2   
def isPalindrome2(s:str)->bool:
    """_summary_
    This version is require less storage space from solution 1
    Where we had to add to the memory few extra lists. 
    But Solution 2 is slower that Solution 1
    """
    l,r = 0, len(s) - 1
    while l < r :
        while l < r and not alphaNum(s[l]):
            l += 1 
        while r > l and not alphaNum(s[r]):
            r -= 1 
        if s[l].lower() != s[r].lower():
            print(s[l], s[r])
            return False
        l += 1 
        r -= 1       
    return True
    
def alphaNum(c):
    # return True if c charactere is inbetween A-Z or a-z or 0-9
    return (ord('A')<= ord(c)<= ord('Z') or
            ord('a')<= ord(c)<= ord('z') or
            ord('0')<= ord(c)<= ord('9'))
    
print(isPalindrome(s), isPalindrome2(s))
