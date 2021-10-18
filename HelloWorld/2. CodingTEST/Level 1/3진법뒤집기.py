class Solution:
    def solutionA(self, n):
        answer = 0
        result = ''
        while n > 0:
            n, result_part = divmod(n, 3)
            result = result + str(result_part)
        answer = int(result, 3)
        return answer

a = Solution()
print(a.solutionA(45))