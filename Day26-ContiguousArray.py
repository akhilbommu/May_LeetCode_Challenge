"""
Problem Link : "https://leetcode.com/problems/contiguous-array/"
"""


class ContinguousArray:
    def findMaxLength(self, nums):
        d = dict()
        d[0] = -1
        max_length, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in d.keys():
                max_length = max(max_length, i - d[count])
            else:
                d[count] = i
        return max_length

obj = ContinguousArray()
print(obj.findMaxLength([0, 1]))
print(obj.findMaxLength([0, 1, 0]))