class Solution:
    def solutionA(self, n):
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a+b
        return b

a = Solution()
print(a.solutionA(5))