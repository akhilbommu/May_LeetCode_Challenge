class PossibleBipartition:
    def possibleBipartition(self, N: int, dislikes):
        d = dict()
        for each in dislikes:
            if each[0] in d:
                d[each[0]].add(each[1])
            else:
                d[each[0]] = set([each[1]])
            if each[1] in d:
                d[each[1]].add(each[0])
            else:
                d[each[1]] = set([each[0]])

        seen = dict()
        for i in range(1, N + 1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while len(stack) != 0:
                    a = stack.pop()
                    if a in d:
                        for b in d[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a] + 1) % 2
                                stack.append(b)
        return True


obj = PossibleBipartition()
print(obj.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
print(obj.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))
print(obj.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
