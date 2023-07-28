''' Given an array of strings strs, group the anagrams together. You can return the answer in any order. '''

''' https://leetcode.com/problems/group-anagrams/ '''

from collections import defaultdict

def groupAnagrams (strs): 
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26 # [0,0,0,0,..........0,0,0]

        for c in s: 
            count[(ord(c) - ord("a"))] += 1

        res[tuple(count)].append(s)

    return(res.values())
            
    


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        
        