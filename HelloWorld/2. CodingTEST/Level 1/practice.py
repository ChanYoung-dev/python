from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in nums:
            print(str(i)[0])

a = Solution()
print(a.largestNumber(nums = [3,30,34,5,9]))