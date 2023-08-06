"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target."""

''' https://leetcode.com/problems/two-sum/ '''


def two_sum(nums, target):
    checked_num_list = []
    for index, num in enumerate(nums):
        required_digit = target - num
        if required_digit in checked_num_list:
            return [checked_num_list.index(required_digit), index]
        else:
            checked_num_list.append(num)


print(two_sum([2, 7, 11, 15], 9))
