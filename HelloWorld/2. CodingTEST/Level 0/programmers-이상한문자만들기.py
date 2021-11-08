class Solution:
    def solutionA(self, s):
        answer = []
        s_split = s.split(" ")
        for s_part in s_split:
            s_part = list(s_part)
            for index in range(0, len(s_part)):
                if not(index%2):
                    if not s_part[index].isupper():
                        s_part[index] = s_part[index].upper()
                else:
                    if not s_part[index].islower():
                        s_part[index] = s_part[index].lower()
            answer.append(''.join(s_part))
        return ' '.join(answer)

a = Solution()
print(a.solutionA("t rY"))