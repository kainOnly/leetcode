class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count, cursor = 0, len(s) - 1
        while cursor >= 0:
            if not s[cursor].isalpha() and count != 0:
                break
            if s[cursor].isalpha():
                count += 1
            cursor -= 1
        return count
