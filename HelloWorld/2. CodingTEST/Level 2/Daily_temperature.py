# 일일 온도
# https://leetcode.com/problems/daily-temperatures/
# page.252



from typing import List

# 내가 푼 풀이법: 시간초과 뜸
'''시간초과
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_num = max(temperatures)
        answer = []

        for index, value in enumerate(temperatures):
            change = False
            if max_num == value:
                answer.append(0)
            else:
                for index2, value2 in enumerate(temperatures[index+1:]):
                    if value < value2:
                        answer.append(index2+1)
                        change = True
                        break
                if change == False:
                    answer.append(0)
        return answer
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                last = stack.pop()
                answer[last] = i-last
            stack.append(i)
        print(answer)


print(Solution().dailyTemperatures(temperatures = [55,38,53,81,61,93,97,32,43,78,32]))