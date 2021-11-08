class Solution:
    def solutionA(self, n):
        answer=''
        for num in range(n):
            answer += "수" if not(num%2) else "박"
        return answer

a = Solution()
print(a.solutionA(4))