from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]
            if nums[i] > m:
                m = nums[i]
        return m
