# 빗물 트래핑
# https://leetcode.com/problems/Trapping_rain_water
# page.180

# 내가 푼 문제풀이
# left부터 빗물을 확인한뒤 가장 큰 벽을 만나면
# right부터 빗물을 확인한다.
# 벽이 두개이면 두개사이에서 위과정을 반복한다.
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = height[left]
        max_right = height[right]
        rain = 0

        while left <= right:
            # left부터 빗물을 확인한뒤 가장 큰 벽을 만나면
            # right부터 빗물을 확인한다.
            while height[left] != max(height):
                #최대높이(max(height))를 만나기 전 최대높이보다 낮은 제일 큰 높이(max_left)를 left 0부터 하나씩 찾는다.
                max_left = max(height[left], max_left)
                rain += (max_left - height[left])
                left += 1
            while ( height[right] != max(height) ) and (left < right):
                # 최대높이(max(height))를 만나기 전 최대높이보다 낮은 제일 큰 높이(max_right)를 right 0부터 하나씩 찾는다.
                max_right = max(height[right], max_right)
                rain += (max_right - height[right])
                right -= 1
            # 최대 높이의 벽(max[height])을 만난뒤부터는 무조건 제일 큰 높이가 max(height)이다.
            left += 1
            max_left = max(height)
            right -= 1
            max_right = max(height)
            # 벽이 두개이면 두개사이에서 위과정을 반복한다.
        return rain

a = Solution()
print(a.trap([2, 0, 2]))