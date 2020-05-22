from collections import Counter
import operator


class SortCharactersByFrequency:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = ""
        sorted_c = dict(sorted(c.items(), key=operator.itemgetter(1), reverse=True))
        for each in sorted_c:
            res += each * c[each]
        return res

obj = SortCharactersByFrequency()
print(obj.frequencySort("tree"))
print(obj.frequencySort("cccaaa"))
print(obj.frequencySort("Aabb"))
print(obj.frequencySort("abcaba"))
