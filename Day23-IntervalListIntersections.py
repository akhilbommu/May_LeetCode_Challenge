class IntervalListIntersection:

    def intervalIntersection(self, A, B):
        res_list = []
        A_index, B_index = 0, 0

        while A_index < len(A) and B_index < len(B):
            low = max(A[A_index][0], B[B_index][0])
            high = min(A[A_index][1], B[B_index][1])

            if low <= high:
                res_list.append([low, high])

            if A[A_index][1] < B[B_index][1]:
                A_index += 1
            else:
                B_index += 1

        return res_list


obj = IntervalListIntersection()
print(obj.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
