from typing import List
# TODO 暴力法，待完善

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
            if target < num:
                nums.insert(i, target)
                return i
        nums.append(target)
        return len(nums) - 1
