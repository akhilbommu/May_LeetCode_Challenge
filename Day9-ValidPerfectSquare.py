"""
Problem Link : "https://leetcode.com/problems/valid-perfect-square/"

Approach : Binary Search
           # We check if square of mid element is num if so we return True.
           # If square of mid element is greater than num we check in first half so "end=mid-1" else
             we check in last half so "start=mid+1".
"""

class ValidPerfectSquare:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = start + ((end - start) // 2)
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                end = mid - 1
            else:
                start = mid + 1
        return False

obj = ValidPerfectSquare()
print(obj.isPerfectSquare(16))
print(obj.isPerfectSquare(25))
print(obj.isPerfectSquare(48))

