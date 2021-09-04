# 두 정렬 리스트의 병합
# https://leetcode.com/problems/Merge_Two_Sorted_Lists/
# page.213

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next
    return res.next
def WhoisNone(l1: Optional[ListNode], l2: Optional[ListNode]):
    if l1 == None and l2 == None:
        return None
    elif l1 == None and l2 != None:
        return l2
    elif l2 == None and l1 != None:
        return l1
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None or l2 ==None:
            return WhoisNone(l1, l2)

        main = (l2 if (l1.val > l2.val) else l1)
        sub = (l1 if (l1.val > l2.val) else l2)

        head = main

        while sub is not None:
            if main.next == None:
                main.next = sub
                break
            if main.next.val > sub.val:
                sub.next, sub, main.next=main.next,sub.next,sub
                main = main.next
                '''
                new_node = ListNode(sub.val, main.next)
                main.next = new_node
                main = new_node
                sub = sub.next
                '''
            else:
                main = main.next

        main = head
        return main
        ''' 모든 노드 출력
        while main is not None:
            print("main:", main.val)
            main = main.next
        '''



print(Solution().mergeTwoLists(l1 = makeNode([1,2,4]), l2=makeNode([1,3,4,5,6,7])))