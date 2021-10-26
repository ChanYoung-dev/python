class Solution:
    def solutionA(self, absolutes, signs):
        return sum(absolutes[i]*(1 if signs[i] else -1) for i in range(len(signs)))


a = Solution()
print(a.solutionA([4, 7, 12], [True, False, True]))