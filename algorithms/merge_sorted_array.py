from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index, cursor1, cursor2 = m + n - 1, m - 1, n - 1
        while cursor1 >= 0 or cursor2 >= 0:
            if cursor1 == -1:
                nums1[index] = nums2[cursor2]
                cursor2 -= 1
            elif cursor2 == -1:
                nums1[index] = nums1[cursor1]
                cursor1 -= 1
            elif nums1[cursor1] < nums2[cursor2]:
                nums1[index] = nums2[cursor2]
                cursor2 -= 1
            else:
                nums1[index] = nums1[cursor1]
                cursor1 -= 1
            index -= 1
