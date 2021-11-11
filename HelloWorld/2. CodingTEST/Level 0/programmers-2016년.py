class Solution:
    def solutionA(self, a, b):
        month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        total_day = sum(month_day[0:a]) + b
        print(day[(total_day%7)-3])



a = Solution()
print(a.solutionA(5, 24))