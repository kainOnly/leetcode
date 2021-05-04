from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        cusor = 1
        while True:
            if target == nums[left] + nums[cusor]:
                break
            if cusor < right:
                cusor += 1
            else:
                left += 1
                cusor = left + 1
        return [left, cusor]
