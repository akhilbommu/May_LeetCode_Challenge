"""
Problem Link : "https://leetcode.com/problems/find-the-town-judge/"

Approach : Create a dictionary and of with keys in given range from 1 to 'N' (both inclusive) with their values as zeroes.
           Create an array of villagers i.e., first element in each array of trust array.
           Iterate through the trust array and increment the values by 1 in where keys are "trust[i][1]".
           Then iterate through the dictionary and check if for any element in the dictionary if its
           value is equal to "N-1" and that element should not be in villagers array.
           If such element we return that element else return "-1".
"""


class FindTheTownJudge:
    def findJudge(self, N, trust):
        d = dict()
        for i in range(1, N + 1):
            d[i] = 0

        villagers = [trust[i][0] for i in range(len(trust))]

        for i in range(len(trust)):
            d[trust[i][1]] += 1

        for each in d:
            if d[each] == N - 1 and each not in villagers:
                return each
        return -1


obj = FindTheTownJudge()
print(obj.findJudge(2, [[1, 2]]))
print(obj.findJudge(3, [[1, 3], [2, 3]]))
print(obj.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(obj.findJudge(3, [[1, 2], [2, 3]]))
print(obj.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
