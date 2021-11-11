import collections
class Solution:
    def solutionA(self, N, stages):
        dict_stage = collections.defaultdict(int)
        count_num = collections.Counter(stages)
        stages.sort(reverse=True)
        for i in range(1, N+1):
            dict_stage[i] = count_num[i]/len(stages) if len(stages) != 0 else 0
            while len(stages) != 0 and i == stages[-1]:
                stages.pop()
        return sorted(dict_stage, reverse=True, key=dict_stage.get)



a = Solution()
print(a.solutionA(4, [1]))