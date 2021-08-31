# 배열 파티션
# https://leetcode.com/problems/array-partition-i/
# page.190

# 내가 푼 문제 풀이
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum1 = 0
        nums.sort()
        print(nums, type(nums))

        for i in range(0,len(nums)-1):
            if i%2:
                continue
            else:
                sum += min(nums[i], nums[i+1])
        return sum

        #print([min(nums[i], nums[i+1]) for i in range(0, len(nums)-1) if not i%2])
a = Solution()
print(a.arrayPairSum([6,2,6,5,1,2]))
'''
파이썬다운 문제 풀이
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2]
'''