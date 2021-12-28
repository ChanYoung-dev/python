class Solution:
    def solution(self):
        num = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        print(a)
        check = -1
        for idx, value in enumerate(a):
            check = max(idx + 2 + value, check)
        return check



a=Solution()
print(a.solution())
#그리드