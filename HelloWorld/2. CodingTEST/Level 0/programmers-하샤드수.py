class Solution:
    def solutionA(self, x):
        return not(x % sum([int(num) for num in str(x)]))

a = Solution()
print(a.solutionA(18))