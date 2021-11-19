# 구간 병합
# https://leetcode.com/problems/merge-intervals/
# page.497


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intv = sorted(intervals, key=lambda x:x[0])
        answer = [intv[0]]
        for value in intv[1:]:
            if answer[-1][1] >= value[0]:
                answer[-1]=[answer[-1][0], max(value[1], answer[-1][1])]
            else:
                answer.append(value)
        return answer

a = Solution()
print(a.merge(intervals = [[0,2],[1,4],[3,5]]))