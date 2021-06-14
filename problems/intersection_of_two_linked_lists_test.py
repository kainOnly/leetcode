import unittest
from .intersection_of_two_linked_lists import Solution, ListNode


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def create(self, queue: list):
        queue = queue[::-1]
        L = ListNode(queue.pop())
        cursor = L
        while len(queue) != 0:
            node = ListNode(queue.pop())
            cursor.next = node
            cursor = cursor.next
        return L

    def walk(self, L: ListNode):
        while L:
            if not L:
                break
            print(L.val)
            L = L.next

    def test_example1(self):
        listA = self.create([4, 1, 8, 4, 5])
        listB = self.create([5, 0, 1, 8, 4, 5])
        self.assertEqual(self.sol.getIntersectionNode(listA, listB).val, 8)
