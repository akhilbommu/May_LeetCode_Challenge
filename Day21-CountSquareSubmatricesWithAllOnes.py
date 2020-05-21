"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""


class CountSquareSubmatricesWithAllOnes:

    def countSquares(self, matrix):
        dp_result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(matrix)):
            dp_result[i][0] = matrix[i][0]

        for j in range(len(matrix[0])):
            dp_result[0][j] = matrix[0][j]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp_result[i][j] = 1 + min(dp_result[i - 1][j], dp_result[i][j - 1], dp_result[i - 1][j - 1])

        submatrices_result = 0

        for each in dp_result:
            submatrices_result += sum(each)

        return submatrices_result


obj = CountSquareSubmatricesWithAllOnes()
print(obj.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
print(obj.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
