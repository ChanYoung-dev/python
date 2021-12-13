class Solution:
    def solution(self, A, B):
        return sum([i[0] * i[1] for i in zip(sorted(A, reverse=False), sorted(B, reverse=True))])

a=Solution()
print(a.solution([1, 4, 2], [5, 4, 4]))