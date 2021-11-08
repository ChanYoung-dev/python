class Solution:
    def solutionA(self, n):
        count = 0
        for number in range(2, n+1):
            for is_sosu in range(2, int(number**(0.5))+1):
                if not(number%is_sosu):
                    break
            else:
                count += 1
        return count
a = Solution()
print(a.solutionA(10))