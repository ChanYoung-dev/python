# 그룹 에너그램
# https://leetcode.com/problems/group-anagrams/
# page.153

# 푸는 원리
'''
s = 'zfdsw'
        s1 = 'fsdwz'
        print(''.join(sorted(s))) # dfswz
        print(''.join(sorted(s1))) # dfswz

'''

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        print(anagrams)
        #defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})


        #return anagrams.values() #ValuesView[list] 형식으로 반환되기때문에
        # dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])


        return list(anagrams.values())
        #[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
