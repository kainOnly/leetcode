from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] + [0] * rowIndex
        for y in range(1, rowIndex + 1):
            x = y
            while x > 0:
                row[x] += row[x - 1]
                x -= 1
        return row
