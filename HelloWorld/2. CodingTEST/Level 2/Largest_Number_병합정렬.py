# page 504
# https://leetcode.com/problems/largest-number/
# 병합정렬
from typing import List

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if str(high_arr[h]) + str(low_arr[l]) < str(low_arr[l]) + str(high_arr[h]):
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(map(str, merge_sort(nums)))))

a = Solution()
print(a.largestNumber(nums = [3,30,34,5,9]))
