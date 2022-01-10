import collections

length = int(input())
arrays = [list(map(int, input().split(' '))) for _ in range(length)]
result = collections.defaultdict(int)
class Solution:
    def solution(self):
        def func(x, y, num):
            for array in arrays[x:x+num]:
                for value in array[y:y+num]:
                    if arrays[x][y] != value:
                        num = int(num/3)
                        for n in range(0, num*2+1, num):
                            for m in range(0, num*2+1, num):
                                func(x+n, y+m, num)
                        return
            else:
                result[arrays[x][y]] += 1
                return
        func(0, 0, length)
        return str(result[-1]) + '\n' + str(result[0]) + '\n' + str(result[1])
a = Solution()
print(a.solution())
# 재귀
# 이걸 참고하자
# https://suri78.tistory.com/69
# 좋음