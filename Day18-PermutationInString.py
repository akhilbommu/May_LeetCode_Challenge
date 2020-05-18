from collections import Counter
class PermutationInString:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            if Counter(s1) == Counter(s2[i:i+len(s1)]):
                return True
        return False

obj = PermutationInString()
print(obj.checkInclusion("ab", "eidbaooo"))
print(obj.checkInclusion("ab", "eidboaoo"))