class Solution:
    def solutionA(self, numbers):
        result = list(range(0, 10))
        for number in numbers:
            result.remove(number)
        return sum(result)

a = Solution()
print(a.solutionA([1,2,3,4,6,7,8,0]))