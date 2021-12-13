import copy
class Solution:
    def solutionA(self, land):
        answer = 0
        n = len(land)

        for i in range(1, n):
            land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
            land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
            land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
            land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

        answer = max(land[n - 1])

        return answer





a = Solution()
print(a.solutionA([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))