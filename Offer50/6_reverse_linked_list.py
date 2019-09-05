""" [翻转单链表](https://www.lintcode.com/problem/reverse-linked-list/description?_from=ladder&&fromId=6)
翻转一个链表
"""


class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
