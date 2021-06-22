class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ''
        while columnNumber:
            columnNumber -= 1
            column = chr(65 + columnNumber % 26) + column
            columnNumber //= 26
        return column
