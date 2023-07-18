# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once

s = "IAmLordVoldemort"
t = "TomMarvoloRiddle"

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    s = list(s.lower()) # transform sting to lowercase and to list
    t = list(t.lower())
    for letter in t:
        s.remove(letter) # for each letter in t remove the corresponding letter in s

    if len(s) == 0: return True # If no letter left = anagram 
    else: return False     
     

print(isAnagram(s,t))