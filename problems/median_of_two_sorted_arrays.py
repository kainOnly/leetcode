from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length == 0:
            return float(0)
        odd = length % 2 != 0
        k = (length + 1) // 2
        while True:
            if len(nums1) == 0:
                return nums2[k - 1] if odd else (nums2[k - 1] + nums2[k]) / 2
            if len(nums2) == 0:
                return nums1[k - 1] if odd else (nums1[k - 1] + nums1[k]) / 2
            if k == 1:
                break

            cursor = k // 2 - 1
            if nums1[cursor] < nums2[cursor]:
                nums1 = nums1[cursor + 1:]
            else:
                nums2 = nums2[cursor + 1:]
            k -= k // 2
        if odd:
            return min(nums1[0], nums2[0])
        else:
            print(nums1, nums2)
            if len(nums1) + len(nums2) == 2:
                return (nums1[0] + nums2[0]) / 2
            if len(nums1) > len(nums2):
                tmp = nums1
                nums1 = nums2
                nums2 = tmp
            if nums1[0] > nums2[0]:
                return (nums2[0] + nums2[1] if len(nums2) > 1 else nums2[0] + nums1[0]) / 2
            else:
                return (nums1[0] + nums1[1] if len(nums1) > 1 else nums1[0] + nums2[0]) / 2
