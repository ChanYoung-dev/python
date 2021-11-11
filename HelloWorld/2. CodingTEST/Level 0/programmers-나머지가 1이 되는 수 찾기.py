class Solution:
    def solutionA(self, n):
        for i in range(2,n):
            if n%i == 1:
                return i

a = Solution()
print(a.solutionA(5))