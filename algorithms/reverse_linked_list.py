# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self) -> List:
        cursor = self
        values = []
        while cursor:
            values.append(cursor.val)
            cursor = cursor.next
        return values


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        while head:
            cursor = ListNode(head.val)
            if reverse:
                cursor.next = reverse
            reverse = cursor
            head = head.next
        return reverse
