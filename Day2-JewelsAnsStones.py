"""
Problem Link: "https://leetcode.com/problems/jewels-and-stones/"
"""

"""
Approach : Create a dictionary of charcaters of 'S'.Then iterate through each character of string 'J' and
            get the value of that particular character and add it to count and finally return the count.
"""


class JewelsAndStones:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = dict()
        for ch in S:
            if ch in d.keys():
                d[ch] += 1
            else:
                d[ch] = 1
        count = 0

        for ch in J:
            if ch in d.keys():
                count += d[ch]
        return count


obj = JewelsAndStones()
print(obj.numJewelsInStones("aA", "aAAbbbb"))
