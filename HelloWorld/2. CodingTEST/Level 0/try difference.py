import re


class Solution:
    def solution(self, data):
        data = [1, 2, 3]

        for i in range(len(data) + 1):
            if i >= len(data):
                break
            print(data[i])

        for i in range(len(data) + 1):
            try:
                print(data[i])
            except:
                break


a = Solution()
print(a.solution('11111'))
# 그리드