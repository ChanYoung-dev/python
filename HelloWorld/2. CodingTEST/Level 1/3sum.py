from itertools import combinations
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for num in combinations(nums, 3):
            if sum(num) == 0:
                result.add(tuple(num))

        return result

a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))