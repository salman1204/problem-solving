'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. '''

''' https://leetcode.com/problems/top-k-frequent-elements/ ''' 

import heapq

def topKFrequent (nums,k):
    dict = {}
    
    for num in nums:
        if num in dict:
            dict[num] +=1
        else:
            dict[num] = 1
            
    top_two = heapq.nlargest(k, dict, key=dict.get)
    return top_two

print(topKFrequent([1,2,3,1,4,1,2,2],2))