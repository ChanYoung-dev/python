import heapq
import sys
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(x[0],-x[1]))
        result = []
        while people:
            person = people.pop()
            result.insert(person[1], [person[0],person[1]])
        return result
a=Solution()
print(a.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))