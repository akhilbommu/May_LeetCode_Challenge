"""
Problem Link : "https://leetcode.com/problems/majority-element/"

Approach 1 : Create a dictionary object and iterate through it and check if value of particular element is
             greater than "math.floor(len(nums) / 2" if so return that element.

Approach 2 : Sort the given array.For an element to be a majority element its occurances should be greater than
             half the length of given array.
             So when we sort the array the majority element will be at the index "len(nums)//2".
"""

import math
from collections import Counter


class MajorityElement:

    def majorityElement1(self, nums):
        d = Counter(nums)
        for each in d:
            if d[each] > math.floor(len(nums) / 2):
                return each

    def majorityElement2(self, nums):
        nums = sorted(nums)
        return nums[len(nums) // 2]


obj = MajorityElement()
nums = [1, 2, 3, 4, 1, 2, 2, 2, 2, 2]
print(obj.majorityElement1(nums))
print(obj.majorityElement2(nums))
