from functools import reduce


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda x, y: x * 26 + y, [ord(char) - 64 for char in columnTitle])
