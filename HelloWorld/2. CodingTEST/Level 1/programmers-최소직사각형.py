class Solution:
    def solutionA(self, sizes):
        a = max(i[0] for i in sizes)
        b = max(i[1] for i in sizes)
        sizes = ([[i[1], i[0]] if i[0] < i[1] else [i[0], i[1]] for i in sizes]) if a > b else ([[i[1], i[0]] if i[0] > i[1] else [i[0], i[1]] for i in sizes])
        return max(i[0] for i in sizes)*max(i[1] for i in sizes)

a = Solution()
print(a.solutionA([[60, 50], [30, 70], [60, 30], [80, 40]]))