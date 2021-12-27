import collections
import heapq
import sys
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        while True:
            print(counter.most_common(n+1))
            sub_count = 0
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                print(task, _)
                counter.subtract(task)
                counter += collections.Counter()
            if not counter:
                break
            for i in range(n - sub_count +1):
                print("idle")
            result += n - sub_count + 1
            print(result)
            print(counter)
        return result
a=Solution()
print(a.leastInterval(tasks = ["A","A","A","B","C","D"], n = 2))