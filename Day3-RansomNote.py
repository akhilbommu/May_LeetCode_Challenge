"""
Problem Link : "https://leetcode.com/problems/ransom-note/"
"""

"""
def returnDict(string):
    dict_ = dict()
    for each in string:
        if each in dict_.keys():
            dict_[each] += 1
        else:
            dict_[each] = 1
    return dict_
def canConstruct(note, magazine):
    if note == "":
        return True
    dict_m = returnDict(magazine)
    dict_n = returnDict(note)
    flag = 0
    for key in dict_n:
        if key in dict_m and dict_n[key] <= dict_m[key]:
            flag = 1
        else:
            flag = 0
            break
    if (flag == 1):
        return True
    else:
        return False
"""
import collections
def canConstruct(note, magazine):
    dict_m = collections.Counter(magazine)
    dict_n = collections.Counter(note)
    for char, count in dict_n.items():
        if dict_m[char] < count:
            return False
    return True
note = input()
magazine = input()
print(canConstruct(note,magazine))
