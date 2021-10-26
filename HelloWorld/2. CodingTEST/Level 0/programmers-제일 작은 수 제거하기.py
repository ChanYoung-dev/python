class Solution:
    def solutionA(self, arr):
        arr.remove(min(arr))
        return arr if len(arr) else [-1]

a = Solution()
print(a.solutionA([1]))