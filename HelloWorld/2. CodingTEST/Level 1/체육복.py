class Solution:
    def solutionA(self,n, lost, reverse):
        for i in list(set(lost) & set(reverse)):
            lost.remove(i)
            reverse.remove(i)
        lost.sort()
        for i in lost[-1::-1]:
            if i - 1 in reverse or i+1 in reverse:
                lost.remove(i)
                if i + 1 in reverse:
                    reverse.remove(i + 1)
                else:
                    reverse.remove(i - 1)
        return n - len(lost)



a = Solution()
print(a.solutionA(5, [2, 3, 4], [3, 4, 5]))