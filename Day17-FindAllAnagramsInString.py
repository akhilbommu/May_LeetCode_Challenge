"""
Problem Link : "https://leetcode.com/problems/find-all-anagrams-in-a-string/"
"""

class AnagramsInString:
    def findAnagrams(self, s: str, p: str):
        p = sorted(p)
        result = []
        if len(s)<20100 and len(p)<20100:
            for i in range(len(s)-len(p)+1):
                temp = sorted(s[i:i+len(p)])
                if temp == p:
                    result.append(i)
            return result

obj = AnagramsInString()
print(obj.findAnagrams("cbaebabacd", "abc"))
print(obj.findAnagrams("abab", "ab"))