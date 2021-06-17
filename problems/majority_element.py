from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, m = 0, None

        for num in nums:
            if count == 0:
                m = num
            count += -1 if m != num else 1

        return m
