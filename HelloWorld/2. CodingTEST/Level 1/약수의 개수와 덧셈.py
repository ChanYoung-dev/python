class Solution:
    def solutionA(self, left, right):
        sum = 0
        for num in range(left, right+1):
            part_sum = 0
            for i in range(1, num//2 + 1):
                if not num % i:
                    part_sum += 1
            sum += num if part_sum % 2 else -num
        return sum


a = Solution()
print(a.solutionA(13, 17))