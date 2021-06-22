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
    def mergeTwoLists(self, l1, l2) -> ListNode:
        l3 = cursor = ListNode()
        while l1 and l2:
            node = ListNode()
            if l1.val < l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            cursor.next = node
            cursor = node
        cursor.next = l1 if not l2 else l2
        return l3.next
