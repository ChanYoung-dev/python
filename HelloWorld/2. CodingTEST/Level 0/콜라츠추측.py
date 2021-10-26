class Solution:
    def solutionA(self, num):
        result = 0
        while num != 1 and result <= 500:
            num = num/2 if not(num % 2) else num*3+1
            result += 1
        return result if result <= 500 else -1

a = Solution()
print(a.solutionA(626331))