from itertools import permutations
class Solution:
    def solution(self):
        nums = sorted((input()), reverse=True)
        return int(''.join(nums)) if (sum(list(map(int, nums))) % 3 == 0 and nums[-1] == '0') else -1

a=Solution()
print(a.solution())
#그리드
#수학문제