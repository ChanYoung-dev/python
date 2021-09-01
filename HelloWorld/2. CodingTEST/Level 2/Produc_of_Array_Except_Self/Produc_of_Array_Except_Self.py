from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = 1
        p1_list = []
        result_list = []
        for i in range(0, len(nums)):
            p1_list.append(p1)
            p1 *= nums[i]
        p2 = 1
        for i in range(len(nums)-1, 0 -1, -1):
            print("i:", i)
            p1_list[i] = p1_list[i] * p2
            p2 *= nums[i]
        return p1_list


a = Solution()
print(a.productExceptSelf([1,2,3,4]))