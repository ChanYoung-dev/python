class Solution:
    def solutionA(self, seoul):
        return "김서방은 "+str(seoul.index("Kim"))+"에 있다."
a = Solution()
print(a.solutionA(["Jane", "Kim"]))