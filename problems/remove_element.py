from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cursor1, cursor2 = 0, len(nums)
        while cursor1 < cursor2:
            if nums[cursor1] == val:
                nums[cursor1] = nums[cursor2 - 1]
                cursor2 -= 1
            else:
                cursor1 += 1
        return cursor1
