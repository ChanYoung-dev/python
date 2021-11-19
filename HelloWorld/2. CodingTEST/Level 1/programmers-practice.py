import re
class Solution:
    def solutionA(self, skill, skill_trees):
        count = 0
        for skills in skill_trees:
            pattern = ''.join(re.findall('[' + skill + ']', skills))
            count += 1 if len(pattern)>0 and (pattern not in skill or skill[0] != pattern[0]) else 0
            '''
            try:
                count += 1 if pattern not in skill or skill[0] != pattern[0] else 0
            except:
                count += 0
            '''
        return len(skill_trees) - count


a = Solution()
print(a.solutionA("Z", ["BACDE", "CBADF", "AECB", "BDA"]))