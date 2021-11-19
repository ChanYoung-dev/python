class Solution:
    def solutionA(self, s):
        s_list = s.lower().split(' ')
        answer = []
        print(s_list)
        for slist in s_list:
            if len(slist) == 0:
                answer.append('')
            elif len(slist) == 1:
                answer.append(slist[0].upper())
            else:
                answer.append(slist[0].upper() + slist[1:])
        print(s)
        print(answer)
        return ' '.join(answer)


a = Solution()
print(a.solutionA("   aaaaaa3fef     bbbaaa   "))