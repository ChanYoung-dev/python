import collections
from itertools import *

matrix_len = int(input())
arrays = [list(map(int, input().split(' '))) for _ in range(matrix_len)]
score = collections.defaultdict(int)
result = collections.defaultdict(int)
answer = collections.defaultdict(int)
num_array = list(range(matrix_len))
class Solution:
    def solution(self):
        n = 0
        print(num_array)
        for i in list(permutations(num_array,2)):
            print(list(i))
            print(arrays[i[0]][i[1]])
            print((sorted(list(i))))
            print("tuple", tuple(sorted(i)))
            score[tuple(sorted(i))] += (arrays[i[0]][i[1]])
        for i in combinations(num_array, int(matrix_len/2)):
            if tuple(set(num_array)-set(i)) in list(result.keys()):
                print("i", i, "는 이미 있습니다")
                break
            print(i)
            for j in combinations(list(i), 2):
                print(j, "=", score[j])
                result[i] += score[j]
            for k in combinations(list(tuple(set(num_array) - set(i))), 2):
                print(k, "=", score[k])
                result[i] -= score[k]
            result[i] = abs(result[i])
        print("n", n)
        print("result=", result)
        print(score)
        #print(answer)
        return min(list(result.values()))

a = Solution()
print(a.solution())
# 재귀
# 이걸 참고하자
# https://suri78.tistory.com/69
# 좋음