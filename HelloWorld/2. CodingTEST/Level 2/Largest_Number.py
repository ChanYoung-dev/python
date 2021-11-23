# page 504
# https://leetcode.com/problems/largest-number/

from typing import List

def compare(n, m):
    return str(n) + str(m) < str(m) + str(n)


def insert_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and compare(array[j-1], array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(map(str, insert_sort(nums)))))

a = Solution()
print(a.largestNumber(nums = [3,30,34,5,9]))