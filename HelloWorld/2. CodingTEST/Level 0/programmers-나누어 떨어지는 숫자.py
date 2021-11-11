class Solution:
    def solutionA(self, arr, divisor):
        return sorted([num for num in arr if not (num % divisor)]) or [-1]
a = Solution()
print(a.solutionA([2, 36, 1, 3], 5))