# 주식을 사고팔기 가장 좋은 시점
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# page.195
from typing import List


# 브루트 포스로 계산 Time out

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gap_list = [0]
        for i in range(0, len(prices)-1):
            gap_list.append(max(prices[i+1:])-prices[i])
        print(gap_list)
        return max(gap_list)
a = Solution()
print(a.maxProfit(prices = [1,2]))



#책에서 힌트를 갖고 품
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        for i in prices[1:]:
            if(min > i):
                min = i
            elif i-min > max:
                max = i-min
            else:
                continue
        return max

a = Solution()
print(a.maxProfit(prices = [7, 1, 5, 3, 6, 4]))
