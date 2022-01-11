import collections
from itertools import *

matrix_len = int(input())
arrays = [list(map(int, input().split(' '))) for _ in range(matrix_len)]
score = collections.defaultdict(int)
result = collections.defaultdict(int)
num_array = list(range(matrix_len))
class Solution:
    def solution(self):
        for i in list(permutations(num_array, 2)):
            score[tuple(sorted(i))] += (arrays[i[0]][i[1]])
        for i in combinations(num_array, int(matrix_len/2)):
            team_a = set(i)
            team_b = set(num_array) - set(i)
            if tuple(team_b) in result:
                break
            for j in combinations(list(team_a), 2):
                result[i] += score[j]
            for k in combinations(list(team_b), 2):
                result[i] -= score[k]
            result[i] = abs(result[i])
        return min(result.values())

a = Solution()
print(a.solution())
# 분할정복