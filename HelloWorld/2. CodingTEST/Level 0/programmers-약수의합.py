class Solution:
    def solutionA(self, n):
        return sum([num for num in range(1, n//2+1) if not n%num])+n

a = Solution()
print(a.solutionA(5))