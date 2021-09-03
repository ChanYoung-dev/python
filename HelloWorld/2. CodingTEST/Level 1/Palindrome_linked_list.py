# 팰린드롬 연결 리스트
# https://leetcode.com/problems/palindrome-linked-list/
# page.201

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

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list : List = []
        if not head:
            return True

        node = head

        while node is not None:
            node_list.append(node.val)
            node = node.next
        while len(node_list) > 1:
            if node_list.pop(0) != node_list.pop():
                return False
        return True

print(Solution().isPalindrome(head = makeNode([1,2 ])))