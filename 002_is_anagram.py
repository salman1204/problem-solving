'''Given two strings s and t, return true if t is an anagram of s, and false otherwise. '''

''' https://leetcode.com/problems/valid-anagram/ '''

def isAnagram(s,t):
    return sorted(s)==sorted(t)

print(isAnagram("cat","acttt"))