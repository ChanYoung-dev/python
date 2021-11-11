class Solution:
    def solutionA(self, price, money, count):
        return sum([(i+1)*price for i in range(count)])-money if sum([(i+1)*price for i in range(count)])-money > 0 else 0

a = Solution()
print(a.solutionA(3, 35, 4))