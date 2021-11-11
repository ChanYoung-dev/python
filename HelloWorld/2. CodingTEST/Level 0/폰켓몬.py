class Solution:
    def solutionA(self, nums):
        return len(set(nums)) if len(nums)/2 >= len(set(nums)) else len(nums)/2



a = Solution()
print(a.solutionA([3,3,3,2,2,2]))