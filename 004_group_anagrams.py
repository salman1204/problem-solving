import collections

''' Given an array of strings strs, group the anagrams together. You can return the answer in any order. '''

''' https://leetcode.com/problems/group-anagrams/ '''


def group_anagrams(strs):
    res = collections.defaultdict(list)  # defining a dict with the value as list

    for s in strs:
        count = [0] * 26  # [0,0,0,0,..........0,0,0]

        for c in s:
            count[(ord(c) - ord("a"))] += 1

        res[tuple(count)].append(s)  # List can't be a key of a dict

    return res.values()


print(list(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
