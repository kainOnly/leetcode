# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def values(self):
        val = [self.val]
        cursor = self
        while cursor.next:
            cursor = cursor.next
            val.append(cursor.val)
        return val


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, cursor = head, head
        while cursor.next:
            cursor = cursor.next
            if cursor.val != prev.val:
                prev.next = cursor
                prev = cursor
        prev.next = None
        return head
