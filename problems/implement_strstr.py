class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for cursor in range(m - n + 1):
            if haystack[cursor:cursor + n] == needle:
                return cursor
        return -1
