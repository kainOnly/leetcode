from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexs = {}
        for i, num in enumerate(numbers):
            n = i + 1
            other = target - num
            if other in indexs:
                return [indexs[other], n]
            indexs[num] = n
        return []
