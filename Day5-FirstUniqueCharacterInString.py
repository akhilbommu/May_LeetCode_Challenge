"""
Problem Link : "https://leetcode.com/problems/first-unique-character-in-a-string/"

Approach : Create a dictionary object for the given string and store the count of occurences of
           each character into the dictionary (or else use the built-in Counter function to create a dictonary).
           The order will store the characters in the order of their occurence.
           Iterate through each character of string and check the corresponding value of that character in
           the dictionary if it is "1" then return the index of that character. If no such character is found
           we return "-1".
"""

from collections import Counter


class UniqueCharacter:
    def firstUniqChar(self, s: str) -> int:
        string_dic = Counter(s)

        for ind, ch in enumerate(s):
            if string_dic[ch] == 1:
                return ind
        return -1


obj = UniqueCharacter()
print(obj.firstUniqChar("leetcode"))
print(obj.firstUniqChar("eeeee"))
print(obj.firstUniqChar("a"))
