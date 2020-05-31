class EditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_list = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp_list[i][j] = j
                elif j == 0:
                    dp_list[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp_list[i][j] = dp_list[i-1][j-1]
                else:
                    dp_list[i][j] = 1 + min(dp_list[i-1][j-1],dp_list[i][j-1],dp_list[i-1][j])
        return dp_list[-1][-1]

obj = EditDistance()
print(obj.minDistance("horse", "ros"))
print(obj.minDistance("intention", "execution"))