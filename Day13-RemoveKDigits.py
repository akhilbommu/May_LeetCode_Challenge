"""
Problem Link : "https://leetcode.com/problems/remove-k-digits/"
"""

class RemoveKDigits:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        remove_count = k
        for curr_ele in num:
            while remove_count and stack and stack[-1] > curr_ele:
                stack.pop()
                remove_count -= 1
            stack.append(curr_ele)
        print(stack)
        res = str(int("".join(stack[:len(num) - k])))
        return res

obj = RemoveKDigits()
"""
print(obj.removeKdigits("1432219", 3))
print(obj.removeKdigits("10200", 1))
print(obj.removeKdigits("10", 2))"""
print(obj.removeKdigits("1234567890", 9))
#print(obj.removeKdigits("112", 1))