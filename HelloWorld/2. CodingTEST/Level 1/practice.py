# 세수의 합
# https://leetcode.com/problems/3sum/
# page.184

import collections
from typing import List

#내가 푼 문제풀이
# [-4, -1, -1, 0, 1, 2]
#  i   j
#  i        j
#  i           j
#  i              j
#  i                 j
#      i    j
#      i       j
# ....
#                 i  j
# 위와 같이 브루트 포스로 계산했지만 시간초과가 떴다..
# 또한 처음부터 정렬해야 편한 것을 생각하지 못했다.

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_dict = dict()
        answer = collections.defaultdict(list)
        k = 0
        for i, val in enumerate(nums):
            num_dict[val] = i
        #print(num_dict)
        real_answer=[]
        for i, val in enumerate(nums):
            k += 1
            nums_k = nums[k:]
            #print(nums_k)
            num_k_dict = dict()
            for j, val2 in enumerate(nums_k):
                num_k_dict[val2] = j
            for j, val2 in enumerate(nums_k):
                print("i[{0}]:{1} j[{2}]:{3}".format(i, j, val, val2))
                if 0-val-val2 in num_k_dict and i != num_dict[0-val-val2] and j != num_k_dict[0-val-val2]:
                    print("정답", val, val2, 0-val-val2)
                    nums_list=[]
                    nums_list.append(str(val))
                    nums_list.append(str(val2))
                    nums_list.append(str(0-val-val2))
                    nums_str = ''.join(sorted(nums_list))
                    print(nums_str)
                    if answer[nums_str]:
                        nums_list.sort()
                        a = 0
                        for answer_list in answer[nums_str]:
                            if answer_list == nums_list:
                                a = 1
                                break
                        if a == 0:
                            print(answer_list, "와", nums_list, "는 다릅니다.")
                            answer[nums_str].append(nums_list)
                    else:
                        nums_list.sort()
                        answer[nums_str].append(nums_list)

        for i in answer.values():
            for j in i:
                print(j)
                real_answer.append(j)
        print(real_answer)
        return real_answer
'''

# 책에서의 풀이




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        for i in range(len(nums)-2):
            #if nums[i] == nums[i+1]:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result



a = Solution()
print(a.threeSum([4,3,5, 6, 7, -15, 2, 9, 32, 11, 14, 9, -3,1,0,1,-15]))