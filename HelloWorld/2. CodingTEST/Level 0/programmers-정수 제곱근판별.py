class Solution:
    def solutionA(self, n):
        return -1 if n**(1/2)-int(n**(1/2)) else (n**(1/2)+1)**2

a = Solution()
print(a.solutionA(4))