
class Solution:
    def solutionA(self, n):
        reverselist = list(str(n))
        reverselist.reverse()
        return list(map(int, reverselist))

a = Solution()
print(a.solutionA(12345))