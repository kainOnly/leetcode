class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        cursor, inc = 0, -1
        for char in s:
            rows[cursor] += char
            # 到达拐角处变更增量符号
            if cursor == 0 or cursor == numRows - 1:
                inc = -inc
            cursor += inc
        return str.join('', rows)
