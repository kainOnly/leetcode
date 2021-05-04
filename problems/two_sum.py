from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in indexs:
                return [indexs[other], i]
            indexs[num] = i
        return []
