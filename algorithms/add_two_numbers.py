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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = cursor = None
        inc = 0

        while l1 is not None or l2 is not None or inc:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + inc
            if val > 9:
                val -= 10
                inc = 1
            else:
                inc = 0

            node = ListNode(val)

            if l3 is None:
                l3 = cursor = node
            else:
                cursor.next = node
                cursor = cursor.next

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

        return l3
