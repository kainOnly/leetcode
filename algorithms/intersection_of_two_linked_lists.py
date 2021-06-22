# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cursorA, cursorB = headA, headB
        while cursorA != cursorB:
            cursorA = cursorA.next if cursorA else headB
            cursorB = cursorB.next if cursorB else headA
        return cursorA
