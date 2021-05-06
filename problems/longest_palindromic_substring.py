class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        for i, char in enumerate(s):
            cursor = 0
            while cursor < i:
                if s[cursor] != char:
                    cursor += 1
                    continue
                sec = s[cursor:i + 1]
                length = i + 1 - cursor
                even = length % 2 == 0
                k = (length + 1) // 2
                isPalindrome = (even and sec[:k] == sec[k:][::-1]) or (even is False and sec[:k] == sec[k - 1:][::-1])
                if isPalindrome and length > len(palindrome):
                    palindrome = sec
                cursor += 1
        return palindrome
