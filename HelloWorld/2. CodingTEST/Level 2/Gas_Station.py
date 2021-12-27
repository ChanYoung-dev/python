import collections
import heapq
import sys
from typing import List

# gv 가 [-2, 3, -2, 3, -2]일 경우
# 뒤에서부터 생각해보면 어느 특정 index에서 gv[index:]가 음수일 경우,
# index~뒤쪽은 전부 정답이 안된다.
# 정답은 하나이기 때문에
# 앞에서부터 처리를 하면 정답이 뜨면 그게 그냥 정답이다.
# 앞에서부터 처리해보면 index가 0일때는 -2 < 0 이므로 start 1 증가
# index 1부터는 -1로 갈일이없다 즉, 정답이다.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gc = [g - c for g, c in zip(gas, cost)]

        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            fuel += gc[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
        return start


a=Solution()
print(a.canCompleteCircuit(gas = [1,7,3,4,1], cost = [3,4,5,1,3]))