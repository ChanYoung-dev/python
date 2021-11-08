class Solution:
    def solutionA(self, s):
        if s[0]=='+':
            return int(s[1:])
        elif s[0]=='-':
            return -1*int(s[1:])
        else:
            return int(s)


a = Solution()
print(a.solutionA("-1234"))