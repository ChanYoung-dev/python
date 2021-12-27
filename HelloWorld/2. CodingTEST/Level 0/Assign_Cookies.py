from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        init_len = len(g)
        g.sort(reverse=True)
        s.sort(reverse=True)
        print(g, s)

        while s and g:
            print(g[-1], s[-1])
            if g[-1] > s[-1]:
                s.pop()
            else:
                s.pop()
                g.pop()
        return init_len - len(g)

a=Solution()
print(a.findContentChildren(g = [100, 50, 1], s = [101, 89, 51, 49, 1]))