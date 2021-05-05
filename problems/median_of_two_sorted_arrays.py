from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        length = m + n
        even = length % 2 == 0

        k = int((length + 1) / 2)
        if m == 0 or n == 0:
            if m == 0:
                return float((nums2[k - 1] + nums2[k]) / 2 if even else nums2[k - 1])
            if n == 0:
                return float((nums1[k - 1] + nums1[k]) / 2 if even else nums1[k - 1])

        i = int(k / 2) - 1
        while k != 1:
            if nums1[i] <= nums2[i]:
                nums1 = nums1[i + 1:]
            else:
                nums2 = nums2[i + 1:]
            k = k - int(k / 2)
            i = int(k / 2) - 1

        if even:
            return float(nums1[0] + nums2[0] if len(nums1) <= len(nums2) else nums1[0] + nums1[1]) / 2
        else:
            return float(nums1[0] if nums1[0] < nums2[0] else nums2[0])
