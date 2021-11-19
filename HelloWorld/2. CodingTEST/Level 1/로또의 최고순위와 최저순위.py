class Solution:
    def solutionA(self, lottos, win_nums):
        count = 0
        for lotto in lottos:
            if lotto in win_nums:
                count += 1
        return [min(6, 7-(count+lottos.count(0))), min(6, 7-(count))]

a = Solution()
print(a.solutionA([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))