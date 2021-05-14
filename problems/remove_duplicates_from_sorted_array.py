from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cursor1 = 1
        cursor2 = 1
        while cursor1 < len(nums):
            if nums[cursor1] != nums[cursor1 - 1]:
                nums[cursor2] = nums[cursor1]
                cursor2 += 1
            cursor1 += 1
        return cursor2
