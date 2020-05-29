"""
Problem Link : "https://leetcode.com/problems/counting-bits/"
"""


class CountingBits:
    def countBits1(self, num: int):
        res_list = []
        for i in range(num+1):
            res_list.append(bin(i).count('1'))
        return res_list

    def countBits2(self, num: int):
        res_list = [0]
        for i in range(1, num + 1):
            res_list.append(res_list[i >> 1] + int(i & 1))
        return res_list

obj = CountingBits()
print(obj.countBits1(2))
print(obj.countBits1(5))
print(obj.countBits2(2))
print(obj.countBits2(5))