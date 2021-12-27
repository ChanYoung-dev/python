import collections
import heapq
import sys
from typing import List

#try except 버전
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))

        while True:
            print("heap 시작", heap)
            array = []
            sub_count = 0
            for i in range(n+1):
                try:
                    countandtask = heapq.heappop(heap)
                    array.append(countandtask)
                    result += 1
                    sub_count += 1
                except:
                    break
            print(array)
            for i in range(n+1):
                try:
                    if array[i][0] != -1:
                        heapq.heappush(heap, (array[i][0] + 1, array[i][1]))
                except:
                    break
            if not heap:
                break
            result += n + 1 - sub_count
            print("heap 끝", heap, "result?", result)

        return result


a=Solution()
print(a.leastInterval(tasks = ["A","A","A","B","C","D"], n = 2))

#try문을 사용안할때
'''
        counter = collections.Counter(tasks)
        result = 0
        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))

        while True:
            #print("heap 시작", heap)
            array = []
            sub_count = 0
            for i in range(n+1):
                result += 1
                sub_count += 1
                countandtask = heapq.heappop(heap)
                array.append(countandtask)
                if not heap:
                    break
            for i in range(n+1):
                if (i > len(array)-1):
                    break
                elif array[i][0] != -1:
                    heapq.heappush(heap, (array[i][0] + 1, array[i][1]))
            if not heap:
                break
            result += n + 1 - sub_count
            #print("heap 끝", heap, "result?", result)

        return result
'''