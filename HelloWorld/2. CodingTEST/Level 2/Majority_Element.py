from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for i in nums:
            counter[i] += 1
            if counter[i] > len(nums):
                return i

a=Solution()
print(a.majorityElement(nums = [2,2,1,1,1,2,2]))