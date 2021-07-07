from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i, x in enumerate(nums):
            if x in hmap and i - hmap[x] <= k:
                return True
            hmap[x] = i
        return False
