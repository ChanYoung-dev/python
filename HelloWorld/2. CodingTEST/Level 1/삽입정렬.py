from typing import List


def insert_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        insert_sort(nums)
        print(nums)

a = Solution()
print(a.largestNumber(nums = [3,30,34,5,9]))