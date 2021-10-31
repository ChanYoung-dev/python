
class Solution:
    def solutionA(self, n):
        return sum(list(map(int, list(str(n)))))

a = Solution()
print(a.solutionA(12345))