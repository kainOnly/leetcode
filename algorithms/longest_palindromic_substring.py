class Solution:
    def longestPalindrome(self, s: str) -> str:
        length, palindrome = len(s), s[0]
        if length < 2:
            return palindrome

        def findPalindrome(i: int, offset: int) -> str:
            section, expand = '', 1
            while True:
                rindex, lindex = i + offset - expand, i + expand
                if rindex < 0 or lindex > length - 1:
                    break
                right, left = s[rindex], s[lindex]
                if right == left:
                    sec = s[rindex:lindex + 1]
                    if len(sec) > len(section):
                        section = sec
                    expand += 1
                else:
                    break
            return section

        cursor = 0
        while cursor < length:
            str1 = findPalindrome(cursor, 0)
            str2 = findPalindrome(cursor, 1)
            p = str1 if len(str1) > len(str2) else str2
            if len(p) > len(palindrome):
                palindrome = p
            cursor += 1
        return palindrome
