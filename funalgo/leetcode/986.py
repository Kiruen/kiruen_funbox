from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i]
            b1, b2 = B[j]
            # if not (A[i][1] < B[j][0] or B[j][1] < A[i][0]):
            if not (a2 < b1 or b2 < a1):
                res.append([max(a1, b1), min(a2, b2)])

            if b2 <= a2:
                j += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    print(Solution().intervalIntersection())
