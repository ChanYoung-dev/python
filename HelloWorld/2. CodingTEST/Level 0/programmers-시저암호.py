class Solution:
    def solutionA(self, s, n):
        s = list(s)
        for index in range(len(s)):
            if s[index].isupper():
                s[index] = chr((ord(s[index])-ord('A')+n) % 26+ord('A'))
            elif s[index].islower():
                s[index] = chr((ord(s[index]) - ord('a') + n) % 26 + ord('a'))

        return ''.join(s)


a = Solution()
print(a.solutionA("   AAAAAaaBZa aaBZa      z    ", 25))