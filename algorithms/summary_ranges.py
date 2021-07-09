from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i, n = 0, len(nums)
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            high = i - 1
            tmp = str(nums[low])
            if low < high:
                tmp += '->' + str(nums[high])
            result.append(tmp)
        return result
