# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
Problem Link: "https://leetcode.com/problems/first-bad-version/"
"""

def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        If mid is the bad version then the first bad version can be before mid so we make end as mid.
        If mid is not the bad version then the bad version will be after mid so make start as mid+1.
        """
        start, end = 0, n
        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
