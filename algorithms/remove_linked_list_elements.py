# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def valueOf(self) -> List:
        data = []
        cursor = self
        while True:
            data.append(cursor.val)
            if cursor.next is None:
                break
            cursor = cursor.next
        return data


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(0)
        node.next = head
        cursor = node
        while cursor.next:
            if cursor.next.val == val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return node.next
