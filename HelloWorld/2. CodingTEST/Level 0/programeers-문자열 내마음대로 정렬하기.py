class Solution:
    def solutionA(self, strings, n):
        return sorted(strings, key = lambda x:(x[n],x))
a = Solution()
print(a.solutionA(["abce", "abcd", "cdx"], 2))