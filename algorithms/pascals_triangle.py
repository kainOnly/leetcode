from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        data = []
        for y in range(numRows):
            row = []
            for x in range(0, y + 1):
                if x == 0 or x == y:
                    row.append(1)
                else:
                    row.append(data[y - 1][x - 1] + data[y - 1][x])
            data.append(row)
        return data
