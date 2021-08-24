# 두 숫자의 합
# https://leetcode.com/problems/two-sum/
# page.159

from typing import List
#브루트 포스 계산
#5283밀리초
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

#딕셔너리사용방법
#딕셔너리는 해시 테이블로 구현되어있기때문에
#시간복잡도가 O(1)이다.
#48밀리초
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 인덱스와 값을 바꾼다. 즉 인덱스를 키값으로 바꾸어준다.
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 딕셔너리 중 타겟에서 첫번째 뺀수와 일치하는 것을 찾아본다.
        for i,num in enumerate(nums):
            print(nums_map)
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target-num]]

a = Solution()
print(a.twoSum([3,2,4], 6))

