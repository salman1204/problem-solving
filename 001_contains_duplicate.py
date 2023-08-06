"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct."""

''' https://leetcode.com/problems/contains-duplicate/ '''


def contains_duplicate(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        else:
            nums_set.add(num)
    return False


print(contains_duplicate([1, 2, 3, 1]))
