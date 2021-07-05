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
        data = []
        while head:
            data.append(head.val)
            head = head.next
        reverse = ListNode(-1)
        cursor = reverse
        while data:
            cursor.next = ListNode(data.pop())
            cursor = cursor.next
        return reverse.next
