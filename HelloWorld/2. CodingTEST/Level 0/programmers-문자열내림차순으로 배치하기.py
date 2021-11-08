class Solution:
    def solutionA(self, s):
        print(''.join(sorted(s, reverse=True)))
a = Solution()
print(a.solutionA("Zbcdefag"))