class Solution:
    def solution(self):
        data = int(input())
        for five in range(data // 5, -1, -1):
            result = 0
            test = data
            for i in [5, 3]:
                div = five if i == 5 else test//i
                result += div
                test -= div * i
            if test == 0:
                return result
        return -1


a=Solution()
print(a.solution())
#그리드