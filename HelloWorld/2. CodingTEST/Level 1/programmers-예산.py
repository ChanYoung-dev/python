class Solution:
    def solutionA(self, d, budght):
        sort_d = sorted(d)
        sum_value = sum(sort_d)
        while sum_value > budght:
            sum_value -= sort_d.pop()
        return len(sort_d)



a = Solution()
print(a.solutionA([1, 1], 1))