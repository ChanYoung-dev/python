class Solution:
    def solution(self, s):
        return str(max(map(int, s.split()))) + ' ' + str(min(map(int, s.split())))
a=Solution()
print(a.solution("-1 -2 -3 -4"))