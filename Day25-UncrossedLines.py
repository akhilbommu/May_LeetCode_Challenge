class UncrossedLines:
    def maxUncrossedLines(self, A, B) -> int:
        len_A = len(A)
        len_B = len(B)
        dp_result = []
        for i in range(len_A + 1):
            dp_result.append([0] * (len_B + 1))

        for i in range(len_A + 1):
            for j in range(len_B + 1):
                if i == 0 or j == 0:
                    dp_result[i][j] = 0
                elif A[i - 1] == B[j - 1]:
                    dp_result[i][j] = 1 + dp_result[i - 1][j - 1]
                else:
                    dp_result[i][j] = max(dp_result[i - 1][j], dp_result[i][j - 1])
        return dp_result[-1][-1]


obj = UncrossedLines()
print(obj.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
print(obj.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
print(obj.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
